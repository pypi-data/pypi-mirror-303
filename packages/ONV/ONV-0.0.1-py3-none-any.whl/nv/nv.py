#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# NV_library.py by Oliver Whaites
# A library of functions that are useful when simulating NV systems under Dynamical Decoupling
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np
import qutip
import progressbar as pb
from tqdm import tqdm
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy import random
import pandas as pd
import scipy
from matplotlib.ticker import  AutoMinorLocator
from scipy.signal.windows import gaussian

options = qutip.solver.Options()
options.store_states = True 

"""
OPERATIONS
"""

def params():
    """
    
    Returns the default parameters that define and evaluate the model.
    
    Parameters
    -----------

    
    Returns
    -----------
    
    params: dictionary of parameters required to determine and calculate the model
    
    """

    params = {}
    
    #general physics constants
    params['gamma_e'] = -28.025e9;#Hz/T
    params['gamma_C'] = 10.705e6;#Hz/T
    params['gamma_H'] = 42.577478518e6;#Hz/T
    params['gamma_N'] = 3.077e6;#Hz/T
    params['gamma_14N'] = 3.077e6;#Hz/T
    params['h'] = 6.62607e-34; #kg*m**2/s
    params['mu_red'] = 1e-7;#N/A**2
    params['zfs_NV'] = 2.87e9
    params['k_B'] = 1.380649e-23
    params['Temp'] = 300
    
    # model parameters
    params['B0'] = 403e-4#external magnetic field strength
    params['B_mis'] = np.radians(0)
    params['omegaL'] = 2*np.pi*params['B0']*10.705e6#nuclear larmour frequency
    params['N_nuc'] = 1;#the number of nuclei in the system
    params['Overhauser'] = 0
    
    params['decoherence'] = False
    params['T2'] = 1e-3
    
    
    #pulse protocol parameters
    params['Tp'] = 32e-9#duration of a pi pulse
    params['Omega'] = np.pi/params['Tp']
    params['tau'] = 0#the wait time of the pulse protocol
    params['t_ev'] = 0
    params['delta'] = 0#any pulse error introduced
    params['protocol'] = 'CPMG'
    params['pulse_profile'] = 'inst'
    params['Np'] = 1#number of pulses of protocol
    
    #plotting parameters
    params['Delta'] = 0#the width of a tau sweep
    params['Reps'] = 100
    
    #evolution time average parameters
    params['t_wait'] = 0
    params['t_wait_mu'] = 13e-6;
    params['t_wait_sig'] = 0.5e-6
    params['num_avg'] = 10
    
    #cystal parameters
    params['vecs'] = [[0,0,0],#basis atom
                   [0,0.5,0.5],
                   [0.5,0,0.5],
                   [0.5,0.5,0],
                   [0.25,0.25,0.25],#basis atom
                   [0.25,0.75,0.75],
                   [0.75,0.25,0.75],
                   [0.75,0.75,0.25]]
    #all above are normalised, return to real vectors by *lattice constant
    params['bond_size'] = 1.54e-10;# distance between basis atoms = lattice_constant*sqrt(3)/4
    params['lattice_constant'] = 3.57e-10;


    return params

def plot_params():
    """
    
    Returns the default parameters that are used when plotting
    
    Parameters
    -----------

    
    Returns
    -----------
    
    params: dictionary of parameters required to plot figures
    
    """
    # key parameters for the model, as described in Spearman 2018
    params = {}
    # model parameters
    params['background_color'] = 'white';
    params['text_color'] = 'black';
    params['line_color'] = 'black';
    params['line_style'] = '-';
    params['line_width'] = 2
    params['tick_color'] = 'black'
    params['line_alpha'] = 1
    

    
    return params


species_spin = {'C':int(1/2*2 + 1),
                '14N':int(1*2 + 1),
                'N':int(1/2*2 + 1),
                'NV':int(1/2*2 + 1),
                'NV_full':int(1*2 + 1),
                'e': int(1/2*2 + 1)}

"""
FUNCTIONS FOR GENERAL QM OPERATIONS
"""


#a function that rotates a 3D vector around the x axis anticlockwise by theta radians
def x_rotation(vec,theta):

    Rx = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]]);

    return np.dot(Rx,vec)


#a function that rotates a vector around the y axis anticlockwise by theta radians
def y_rotation(vec,theta,passive = False):

    Ry = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]]);
    if passive == True:
        Ry = Ry.T

    if vec.shape == (3,):

        return np.dot(Ry,vec)
    else:
        return np.array([np.dot(Ry,v) for v in vec])
  
def xy_rotation(vec,theta,phase):
    
    
    ux = np.cos(phase)
    uy = -np.sin(phase)
    uz = 0
    
    c = np.cos(theta)
    s = np.sin(theta)
    
    R = np.array([[c + ux**2*(1 - c),ux*uy*(1 - c) - uz*s,ux*uz*(1 - c) + uy*s],
                  [uy*ux*(1 - c) + uz*s,c + uy**2*(1 - c),uy*uz*(1 - c) - ux*s],
                  [uz*ux*(1 - c) - uy*s,uz*uy*(1 - c) + ux*s,c + uz**2*(1 - c)]])
    
    return R.dot(vec)  
  
# a function which changes the basis of the lattice coordinates to one in line with NV-axis
def change_basis(vec):

    #Two rotations about the z by pi/4 then the x by ...
    vectemp = z_rotation(vec,np.pi/4);
    vectemp = x_rotation(vectemp,np.arctan(np.sqrt(2)));


    return vectemp


#a function that rotates a vector around the z axis anticlockwise by theta radians
def z_rotation(vec,theta):

    Rz = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]]);

    return np.dot(Rz,vec)


def cc_coupling(spin,ref,params = params(),species = 'C'):
    
    x = spin['x'] - ref['x']
    y = spin['y'] - ref['y']
    z = spin['z'] - ref['z']
    
    r = np.sqrt(x**2 + y**2 + z**2); #distance between atoms

    const = -(params['h']/(2*np.pi))*params['mu_red']*(2*np.pi*params['gamma_{}'.format(species)])**2/(r**3);

    Cij = const*(3*(z**2)/(r**2) - 1);
    
    return Cij/(2*np.pi)


#function to find the hyperfine coupling constants between the vacancy and a particular atom in the lattice
def hyperfine(r,params = params(),species = 'C'):
#r must be introdued in Angstoms
    x = r[0]*1e-10;
    y = r[1]*1e-10;
    z = r[2]*1e-10;


    r = np.sqrt(x**2 + y**2 + z**2); #distance between atoms

    const = -(params['h']/(2*np.pi))*params['mu_red']*2*np.pi*params['gamma_e']*2*np.pi*params['gamma_{}'.format(species)]/(r**3);

    #find the coupling constants in units kHz*2pi/T
    Ax = const*(3*z*x/(r**2))*1e-3;
    Ay = const*(3*z*y/(r**2))*1e-3;
    Az = const*(3*(z*z)/(r**2) - 1)*1e-3;

    A = [Ax/(2*np.pi),Ay/(2*np.pi),Az/(2*np.pi)];

    return A


#returns the density matrix for a qubit up state 
def rhoU():
    
    return qutip.Qobj([[1,0],[0,0]]);

#returns the density matrix for a qubit down state 
def rhoD():
    
    return  qutip.Qobj([[0,0],[0,1]]);

#returns the density matrix for a qubit Xp state 
def rhoXp():
    
    return (1/2)*qutip.Qobj([[1,1],[1,1]]);

#returns the density matrix for a qubit X- state 
def rhoXm():
    
    return (1/2)*qutip.Qobj([[1,-1],[-1,1]]);

#returns the density matrix for a qubit in a thermal state
def rhoT(params = params(), species = 'C'):
    
    s = species_spin[species]
    
    r =(-(params['h']*params[f'gamma_{species}']*params['B0']*Iz(s))/(2*np.pi*params['k_B']*params['Temp'])).expm();

    return r/r.tr()
#returns the density matrix for a qubit in a thermal state
def rhoSup(a = np.cos(2*np.pi/3),b = np.sin(2*np.pi/3)):
    
    A = (a + b)**2
    B = (a - b)**2
    AB = (a**2 - b**2)
    
    return (1/2)*qutip.Qobj([[A,AB],[AB,B]]);

#A function which returns the reduced quibit Qobj for Sx
def qubit_Sx():

    return qutip.Qobj(np.array([[0,1/2],[1/2,0]]));

#A function which returns the reduced quibit Qobj for Sz in ms = {0,-1} space
def qubit_Szp():

    return qutip.Qobj(np.array([[0,0],[0,1]]));

def qubit_Szm():

    return qutip.Qobj(np.array([[0,0],[0,-1]]));

#A function which returns the reduced quibit Qobj for Sz
def qubit_Sy():

    return qutip.Qobj(np.array([[0,-1j/2],[1j/2,0]]));

#A function which returns the reduced quibit Qobj for Sx
def state_3_Sx():

    return qutip.Qobj((1/np.sqrt(2))*np.array([[0,1,0],[1,0,1],[0,1,0]]));

#A function which returns the reduced quibit Qobj for Sz
def state_3_Sz():

    return qutip.Qobj(np.array([[1,0,0],[0,0,0],[0,0,-1]]));

#A function which returns the reduced quibit Qobj for Sz
def state_3_Sy():

    return qutip.Qobj((1/np.sqrt(2))*np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]]));

#A function which returns the quibit Qobj for Ix
def Ix(s = 2):
    
    if s == 2:
        return qutip.Qobj(np.array([[0,1/2],[1/2,0]]));
    
    elif s == 3:
        return state_3_Sx()
    
    else: raise Exception('s = %s is not supported'%s)

#A function which returns the quibit Qobj for Iz
def Iz(s = 2):

    if s == 2:
        return qutip.Qobj(np.array([[1/2,0],[0,-1/2]]));
    elif s == 3:
        return state_3_Sz()
    
    else: raise Exception('s = %d is not supported'%(s))

#A function which returns the reduced quibit Qobj for Sz
def Iy(s = 2):
    if s == 2:
        return qutip.Qobj(np.array([[0,-1j/2],[1j/2,0]]));
    elif s == 3:
        return state_3_Sy()
    
    else: raise Exception('s = %s is not supported'%s)

#function that constructs the spin ith operator in a tensor space size 2^NumSpin
def spin_tensor_operator(NumSpin, i,space_size = None):
    
    """
    function which generates a spin operator of spin i in a NumSpin spin system
    
    Parameters
    ----------
    
        NumSpin: int for the number of spins in tensor space
        i: int for the position of the spin in the tensor space
        
    returns
    _______
    
        array of spin operators:
            Iz: Qobj for the z-directional spin operator.
            Iy: Qobj for the y-directional spin operator.
            Ix: Qobj for the x-directional spin operator. 

    
    """
    if space_size == None:
        space_size = 2*np.ones(NumSpin)
    
    
    I = qutip.identity(int(space_size[0]));
    
    if i == 0:
        
        Ixi = Ix(space_size[i]);
        Iyi = Iy(space_size[i]);
        Izi = Iz(space_size[i]);
        
    else:
        
        Ixi = I;
        Iyi = I;
        Izi = I;
    
    for j in range(1,NumSpin):
        
        I = qutip.identity(int(space_size[j]));
        
        if j == i:
            
            Ixi = qutip.tensor(Ixi,Ix(space_size[j]));
            Iyi = qutip.tensor(Iyi,Iy(space_size[j]));
            Izi = qutip.tensor(Izi,Iz(space_size[j]));
            
        else:
            
            Ixi = qutip.tensor(Ixi,I);
            Iyi = qutip.tensor(Iyi,I);
            Izi = qutip.tensor(Izi,I);
        

    return [Ixi,Iyi,Izi]


Rho = {'up':rhoU,
       'down':rhoD,
       'Xp':rhoXp,
       'Xm':rhoXm,
       'Therm':rhoT,
       'Sup':rhoSup}


def gaussianEnv(t,args):
    """
    
    
    """

    #tw = args['tw']
    #t0 = args['t0'] 


    #r2sigma2 = 1/(2*tw**2)
    #gaussian_pulse = np.exp(-((t-t0)**2)*r2sigma2)
    if args['finite'] == True:
        gaussian_pulse = gaussian(args['num_t'],args['std'])
    else:
        gaussian_pulse = scipy.signal.gausspulse(t,2*np.pi/args['tw'],retenv = True)[1]
        
        
    if args['plot'] == True:
         
        fig,ax = plt.subplots(dpi = 200)
        #ax.plot(x,L)
        y = gaussian_pulse
        ax.plot(np.array(t)*1e9,y,color = 'k',label = 'Gaussian')
        ax.set_ylabel('Amplitude',fontsize = 12)
        ax.set_xlabel('Time (ns)',fontsize = 12)
        i = 0
        for ti, A in zip(t,y):
            if i == 0:
                ax.fill_between(np.array([ti,ti + args['dt']])*1e9,0,A,color = 'blue',alpha = 0.4,edgecolor = 'k',label = 'L Amp')
                i +=1
            else: ax.fill_between(np.array([ti,ti + args['dt']])*1e9,0,A,color = 'blue',alpha = 0.4,edgecolor = 'k')
        ax.legend()
        
    return gaussian_pulse




"""
OPERATOR AND HAMILTONIAN GENERATORS
"""


def generate_operators(Az, Ax,species = None, params = params(), NV_state = 'up', Nuc_state = None,NV_sub = '-'):
    
    """
    function which generates the evolution operators for a particular system
    
    Parameters
    ----------
    
        NV_state: string to describe the initial state of the NV. default is up
        Nuc_state: array of strings with length of the number of spins in the system
                    to describe the state of the NV. Default = None which will 
                    set nuclear states to thermal mixture Therm
        params: dict of system and protocol parameters. Can be retrieved using 
                params() function
        Az: array of floats which contains the parallel coupling for the spins in system
            length of this array determines how many spins there are.
        Ax: array of floats which contains the perpendicular couplings
        N14: boo determining whether to include N14 spin

        
    returns
    _______
    
        dict_operators: dict containing operators under the following labels
        
            Iz: array of Qobjs for the z-directional spin operators. size of array
                is that of the number of spins
            Iy: array of Qobjs for the y-directional spin operators. size of array
                is that of the number of spins
            Ix: array of Qobjs for the x-directional spin operators. size of array
                is that of the number of spins
            Sz: Qobj for the psuedo spin NV z-directional operator. This is in subspace 
                {-1,0}
            Sy: Qobj for the psuedo spin NV y-directional operator. This is in subspace 
                {-1,0}
            Sx: Qobj for the psuedo spin NV x-directional operator. This is in subspace 
                {-1,0}
            H0: Qobj for the free Hamiltonian of the system 
            rho0: Qobj the density matrix for the initial state of the system
            rho0NV: Qobj for the initial density matrix of the NV
            
        params: updated list of parameters, where the N_nuc reflects the length of 
            Az array input
                    
    
    """
    omegaL = params['omegaL'];

    NV_dict = {'-':qubit_Szm(),
               '+':qubit_Szp(),
               '+-':qubit_Szm() + qubit_Szp()}
    
    dict_operators = {}
    #compute the number of nuclei in the system
    N_nuc = len(Az)
    
    params['N_nuc'] = N_nuc
    
    
    if Nuc_state == None:
        Nuc_state = np.full(N_nuc,'Therm');
        
        
    if species == None:
        species = []
        for i in range(params['N_nuc']):
            species.append('C')
    print(species)
    species.insert(0, 'NV')
    space_size = [species_spin[s] for s in species]
    
    rho0 = Rho[NV_state]();
    
    dict_operators['rho0NV'] = Rho[NV_state]();
        
        
    Sx,Sy,Sz = spin_tensor_operator(N_nuc + 1,0,space_size);
    Sz = NV_dict[NV_sub];
    
    I = qutip.identity(space_size[0]);
    
    Ix = [];
    Iy = [];
    Iz = [];
    
    I_op = I
    
    #construct spin operators for nuclei
    for i in range(1,N_nuc + 1,1):
        
        rho0 = qutip.tensor(rho0,Rho[Nuc_state[i - 1]](params,species[i]));
        
        Ixtemp,Iytemp,Iztemp = spin_tensor_operator(N_nuc + 1,i,space_size);
        
        I = qutip.identity(space_size[i])
        
        Ix.append(Ixtemp);
        Iy.append(Iytemp);
        Iz.append(Iztemp);
        
        Sz = qutip.tensor(Sz,I)
        I_op = qutip.tensor(I_op,I)
        
    dict_operators['rho0'] = rho0;
    
    dict_operators['Iz'] = Iz;
    dict_operators['Ix'] = Ix;
    dict_operators['Iy'] = Iy;
    
    dict_operators['Sx'] = Sx;
    dict_operators['Sy'] = Sy;
    dict_operators['Sz'] = Sz;
    
    dict_operators['I'] = I_op
    
    
    #construct free Hamiltonian
    H0 = params['Overhauser']*Sz
    for i in range(N_nuc):
        
        H0 += omegaL*Iz[i] + Az[i]*Sz*Iz[i] + Ax[i]*Sz*Ix[i] #magnetic field term 
      
    dict_operators['H0'] = H0;
    
      
    
    return dict_operators,params


def add_N14(operators,params,couplings,TN = 3):
    """
    
    
    
    
    """
        
    Sz = state_3_Sz()
    Sy = state_3_Sy()
    Sx = state_3_Sx()
    
    Ix,Iy,Iz, = spin_tensor_operator(params['N_nuc'] + 1,params['N_nuc'] + 2)
    
    Ix = qutip.tensor(Ix,Sx)
    Iy = qutip.tensor(Iy,Sy)
    Iz = qutip.tensor(Iz,Sz)
    
    I = qutip.identity(3)
    
    for i in range(params['N_nuc']):
        
        operators['Iz'][i] = qutip.tensor(operators['Iz'][i],I)
        operators['Iy'][i] = qutip.tensor(operators['Iy'][i],I)
        operators['Ix'][i] = qutip.tensor(operators['Ix'][i],I)
    
    operators['Sz'] = qutip.tensor(operators['Sz'],I)
    operators['Sy'] = qutip.tensor(operators['Sy'],I)
    operators['Sx'] = qutip.tensor(operators['Sx'],I)
    
    
    operators['Iz'].append(Iz)
    operators['Iy'].append(Iy)
    operators['Ix'].append(Ix)
    
    operators['I'] = qutip.tensor(operators['I'],I)
    
    params['N_nuc'] += 1
    
    r0 = qutip.Qobj([[1,0,0],[0,1,0],[0,0,1]])
    #r0 = (-state_3_Sz()/TN).expm()

    
    operators['rho0'] = qutip.tensor(operators['rho0'],r0/r0.tr())
    
    Az = -2*np.pi*2.164689e6
    Ax = -2*np.pi*2.632e6
    
    omega = np.sqrt((params['B0']*2*np.pi*params['gamma_N'] + Az/2)**2 + (Ax/2)**2)
    
    # couplings = couplings.append({'Species': 'N',
    #                   'Ax': Ax,
    #                   'Az': Az,
    #                   'omega': omega},ignore_index = True)
    
    couplings = pd.concat([couplings, pd.DataFrame([{'Species': 'N',
                      'Ax': Ax,
                      'Az': Az,
                      'omega': omega}],index = [0])],ignore_index = True)
    
    return operators, params, couplings


def generate_H0(operators,couplings,params):
    
    """
    a function which re-froms the free Hamiltonian for a system of operators
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        couplings: dataframe of Az and Ax couplings of nucleat spins
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        
        
    returns
    -------
    
        H0: a Qobj for the free Hamiltonian
    """
    
    N_nuc = params['N_nuc'];
    #omegaL = params['omegaL']
    
    Iz = operators['Iz']
    Ix = operators['Ix']
    
    Sz = operators['Sz']
        
    #construct free Hamiltonian
    H0 = params['Overhauser']*Sz
    for i in range(N_nuc):
        
        s = couplings.index.tolist()[i]
        
        Ax = couplings['Ax'].loc[s]
        Az = couplings['Az'].loc[s]
        species = couplings['Species'].loc[s]
        
        omegaL = 2*np.pi*params['B0']*params['gamma_%s'%species]
        
        H0 += omegaL*Iz[i] + Az*Sz*Iz[i] + Ax*Sz*Ix[i] #magnetic field term 
    
    operators['H0'] = H0;
    
    

    return operators

def generate_full_H0(operators,couplings,params,CC_coupling = False):
    
    """
    a function which re-froms the free Hamiltonian for a system of operators
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        Az: dataframe for couplings
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
        
    returns
    -------
    
        H0: a Qobj for the free Hamiltonian
    """
    
    
    
    
    N_nuc = params['N_nuc'];

    
    Iz = operators['Iz']
    Ix = operators['Ix']
    Iy = operators['Iy']
    
    
    Sz = operators['Sz']
    Sx = operators['Sx']
    #Sy = operators['Sy']
        
    #construct free Hamiltonian
    H0 = params['Overhauser']*Sz + 2*np.pi*params['B0']*params['gamma_e']*Sz + 2*np.pi*params['gamma_e']*params['B_mis']*Sx + 2*np.pi*params['zfs_NV']*Sz*Sz
    H0p = params['Overhauser']*Sz
    for i in range(N_nuc):
        s1 = couplings.index.tolist()[i]
        
        Ax = couplings['Ax'].loc[s1]
        Az = couplings['Az'].loc[s1]
        
        species = couplings['Species'].loc[s1]
        
        omegaL = 2*np.pi*params['B0']*params['gamma_%s'%species]
        omegaLx = 2*np.pi*params['B_mis']*params['gamma_%s'%species]
        
        H0 += omegaL*Iz[i] +omegaLx*Ix[i] + Az*Sz*Iz[i] + Ax*Sz*Ix[i] #magnetic field term 
        H0p += omegaL*Iz[i] + omegaLx*Ix[i]  + Az*Sz*Iz[i] + Ax*Sz*Ix[i] 
        if CC_coupling == True:
            for j in range(i,N_nuc):
                s2 = couplings.index.tolist()[j]
                
                C = couplings['C{}'.format(s2)].loc[s1]
                if i != j and  abs(C) > 0:
                    H0 += C*(Iz[i]*Iz[j] + Ix[i]*Ix[j] + Iy[i]*Iy[j])
                    H0p += C*(Iz[i]*Iz[j] + Ix[i]*Ix[j] + Iy[i]*Iy[j])
      
    operators['H0'] = H0;
    
    operators['H0_pulse'] =  H0p
    
    return operators







"""
PULSE PROFILES
"""


def inst_pulse(operators,params,rot = np.pi):
    """
    
    
    """
    
    
    #Omega = params['Omega'];
    delta = params['delta'];
    #Tp = (rot + delta)/Omega
    
    Tp = params['Tp']
    Omega = (abs(rot + delta))/Tp
        
    
    UX = (-1j*(np.sign(rot)*Omega*operators['Sx'])*Tp).expm();
    UY = (-1j*(np.sign(rot)*Omega*operators['Sy'])*Tp).expm();
    
    return UX, UY

def square_pulse(operators,params, rot = np.pi):
    """
    
    
    """
    
    #Omega = params['Omega'];
    delta = params['delta'];
    #Tp = (rot + delta)/Omega
    
    Tp = params['Tp']
    Omega = (abs(rot + delta))/Tp
    
    H0 = operators['H0']
    if params['full_H0'] == True:
        H0 = operators['H0_pulse']   

    
    UX = (-1j*(H0 + np.sign(rot)*Omega*operators['Sx'])*Tp).expm();
    UY = (-1j*(H0 + np.sign(rot)*Omega*operators['Sy'])*Tp).expm();
    

    return UX, UY

def gaussian_pulse(operators,params, rot = np.pi, direction = 'x',dt = 1e-9):
    """
    
    
    """
    

    
    Tp = params['Tp']
    tw = Tp/2
    
    
    t = np.linspace(-tw/2,tw/2,100)
    #t = [0 + n*dt for n in range(int(Tp/dt))]
    
    
    H0 = operators['H0']
    if params['full_H0'] == True:
        H0 = operators['H0_pulse']  
    Om =  1.6824844873848788/Tp
    Hp = (2*rot/np.pi)*2*np.pi*Om*operators['S%s'%direction]

    H = [H0,[Hp,gaussianEnv]]
    
    output = qutip.mesolve(H,
                           operators['rho'],
                           t,
                           e_ops = [operators['Sz']],
                           args = {'finite':False,
                                   'tw': tw,
                                   'plot': False},
                           options = options)
    
    operators['rho'] = output.states[-1]

    
    return operators

def gaussian_pulse_finite(operators,params, rot = np.pi,dt = 1e-9):
    """
    
    
    """
    #print('here')
    
    Tp = params['Tp']
    
    Omega = params['Omega']
    #f = (np.abs(rot)/np.pi)
    
    #t,dt = np.linspace(-Tp*f/2,Tp*f/2,int(Tp*f/dt) + 1,restep = True)
    t = [0 + n*dt for n in range(int(Tp/dt))]

    args = {'num_t':len(t),
            'std':len(t)/5,
            'finite':True,
            'plot':False,
            'dt': dt}
    
    env = gaussianEnv(t, args = args)
    
    #A = 2*np.pi*1.0432600729457604/Tp*f
    #A = 2*np.pi/(2*Tp*f)
    A = Omega
    
    H0 = operators['H0']
    if params['full_H0'] == True:
        H0 = operators['H0_pulse']  
    
    UX = operators['I']
    UY = operators['I']
    for i in range(len(t)):
        UX = (-1j*(H0 + A*env[i]*operators['Sx'])*dt).expm()*UX
        UY = (-1j*(H0 + A*env[i]*operators['Sy'])*dt).expm()*UY
        

    
    return UX,UY

pulse_profiles = {'inst': inst_pulse,
            'square': square_pulse,
            'gaussian_finite':gaussian_pulse_finite,
            'gaussian':gaussian_pulse}







"""
PULSE PROTOCOLS
"""


def Free(operators,params,measure,e_ops = [],c_ops = []):
    
    """
    a function which constructs the free evolution operator
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params:  float for free evolution time
        
        
    returns
    -------
    
        U: Qobj for the free evolution
    """
    
    if params['decoherence'] == False:
    
        U0 = (-1j*operators['H0']*params['t_ev']).expm();
        
        rho = U0*operators['rho']*U0.dag()
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
        return coh, rho, U0
        
    elif params['decoherence'] == True:
        t = np.linspace(0,params['t_ev'],50)
        
        output = qutip.mesolve(operators['H0'],operators['rho'],t, e_ops = e_ops,c_ops = c_ops,options = options)
        
    
        return output.expect[0][-1], output.states[-1]
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
    
    

# a function which takes a free evolution operator and pulse operators and returns a packet of CPMG. Note that UX must be a pi/2 pulse
def XY8(operators, params,measure):
    
    """
    a function which constructs the pulse packet for a CPMG sequence using free evolution 
    and pi/2 pulses. pulse errors, delta, may be included as Tp = (np.pi + delta)/2.
    CPMG sequence here is U0*UX*UX*U0*U0*UX*UX*U0
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
        
    returns
    -------
    
        U: Qobj for the CPMG pulse packet
    """
    
    tau = params['tau'];
    profile = params['pulse_profile']
    
    params['t_ev'] = tau/2
    
    #construct the pulse operators
    UX, UY = pulse_profiles[profile](operators,params,rot = np.pi)
    
    if params['decoherence'] == False:
    
        U0 = (-1j*operators['H0']*params['t_ev']).expm();
    
        
        U = (U0*UX*U0*U0*UY*U0*U0*UX*U0*U0*UY*U0*U0*UY*U0*U0*UX*U0*U0*UY*U0*U0*UX*U0)**(params['Np'])
        
     
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    elif params['decoherence'] == True:
        #raise Exception('Decoherence has not been initialised with this pulse protocol.')
        rho = operators['rho0']
        params['t_ev'] = tau
        
        for i in range(params['Np']):
        
            operators['rho'] = rho    
        
            params['t_ev'] = tau/2
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            operators['rho'] = UX*rho*UX.dag()
            
            params['t_ev'] = tau
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UY*rho*UY.dag()
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UX*rho*UX.dag()
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UY*rho*UY.dag()
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UY*rho*UY.dag()
            cho, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UX*rho*UX.dag()
            cho, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UY*rho*UY.dag()
            cho, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = UX*rho*UX.dag()
            params['t_ev'] = tau/2
            cho, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            
            operators['rho'] = rho
        
        coh = (operators['rho']*operators['Sz']).tr().real 
        
        return coh, operators['rho']
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
        
        


# a function which takes a free evolution operator and pulse operators and returns a packet of CPMG. Note that UX must be a pi/2 pulse
def CPMG(operators, params,measure):
    
    """
    a function which constructs the pulse packet for a CPMG sequence using free evolution 
    and pi/2 pulses. pulse errors, delta, may be included as Tp = (np.pi + delta)/2.
    CPMG sequence here is U0*UX*UX*U0*U0*UX*UX*U0
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
        
    returns
    -------
    
        U: Qobj for the CPMG pulse packet
    """
    
    tau = params['tau'];
    profile = params['pulse_profile']
    
    params['t_ev'] = tau/2
    
    if params['decoherence'] == False:
    
        
        U0 = (-1j*operators['H0']*params['t_ev']).expm();
        
        
        UX, UY = pulse_profiles[profile](operators,params,rot = np.pi)
            
        
        U = (U0*UX*U0*U0*UX*U0)**params['Np']
    
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    elif params['decoherence'] == False:
        raise Exception('Decoherence has not been initialised with this pulse protocol.')
        
        
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
        
        

# a function which takes a free evolution operator and pulse operators and returns a packet of CPMG. Note that UX must be a pi/2 pulse
def spin_locking(operators, params,measure):
    
    """
    a function which constructs the pulse packet for a CPMG sequence using free evolution 
    and pi/2 pulses. pulse errors, delta, may be included as Tp = (np.pi + delta)/2.
    CPMG sequence here is U0*UX*UX*U0*U0*UX*UX*U0
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
        
    returns
    -------
    
        U: Qobj for the CPMG pulse packet
    """
    
    Omega = params['Omega'];
    tau = params['tau'];

    
    params['t_ev'] = tau/2

        
    if params['decoherence'] == False:
        #construct the pulse operators
        U = (-1j*(operators['H0'] + Omega*operators['Sx'])*tau).expm();
        
        rho = U*operators['rho']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    
    elif params['decoherence'] == False:
        raise Exception('Decoherence has not been initialised with this pulse protocol.')
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
        
        

# a function which takes a free evolution operator and pulse operators and returns a packet of PulsePol. Note that UX and UY must be pi/2 pulses
def PulsePol(operators,params,measure):
    
    """
    a function which constructs the pulse packet for a PulsePol sequence using free evolution 
    and pi/2 pulses.
    PulsePol sequence here is (UX*U0*UY*UY*U0*UX*UY*U0*UXm*UXm*U0*UY)**2
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
    returns
    -------
    
        U: Qobj for the CPMG pulse packet
    """

    tau = params['tau'];
    profile = params['pulse_profile']
    
    if params['decoherence'] == False:
    
        U0 = (-1j*operators['H0']*tau).expm();
    
        #construct the pulse operators
        UX, UY = pulse_profiles[profile](operators,params,rot = np.pi/2)
    
        
        UXm = (UX).dag()
        UYm = (UY).dag()
        U = (UX*U0*UY*UY*U0*UX*UY*U0*UXm*UXm*U0*UY)**params['Np']
        #U = (UX*U0*UYm*UYm*U0*UX*UY*U0*UX*UX*U0*UY*UX*U0*UY*UY*U0*UX*UY*U0*UXm*UXm*U0*UY)**params['Np']

        
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
    
        return coh,rho, U
    

    elif params['decoherence'] == False:
        raise Exception('Decoherence has not been initialised with this pulse protocol.')
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
        
        

def PulsePol_cam(operators,params,measure):
    
    """
    a function which constructs the pulse packet for a PulsePol sequence using free evolution 
    and pi/2 pulses.
    PulsePol sequence here is (UX*U0*UY*UY*U0*UX*UY*U0*UXm*UXm*U0*UY)**2
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
    returns
    -------
    
        U: Qobj for the CPMG pulse packet
    """
    
    tau = params['tau'];
    profile = params['pulse_profile']
    #Tp = params['Tp']
    Omega = params['Omega']
    
    params['Omega'] = Omega/2
    UX, UY = pulse_profiles[profile](operators,params,rot = np.pi/2)
    
    #params['Tp'] = Tp/2
    params['Omega'] = Omega
    UXp, UYp = pulse_profiles[profile](operators,params,rot = np.pi)
    
    UXm = (UXp).dag()
    
    if params['decoherence'] == False:
    
        U0 = (-1j*operators['H0']*tau).expm();
       

        U = (UX*U0*UYp*U0*UX*UY*U0*UXm*U0*UY)**params['Np']
        
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    elif params['decoherence'] == True:
        rho = operators['rho0']
        params['t_ev'] = tau
        
        for i in range(params['Np']):
        
            operators['rho'] = UY*rho*UY.dag()
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            operators['rho'] = UXm*rho*UXm.dag()
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            operators['rho'] = UX*UY*rho*UY.dag()*UX.dag()
            
  
            coh, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            operators['rho'] = UYp*rho*UYp.dag()
            cho, rho = Free(operators, params, measure,e_ops = [operators['Sz']],c_ops = [(1/np.sqrt(params['T2']))*operators['Sx']])
            operators['rho'] = UX*rho*UX.dag()
            
            rho = operators['rho']
            
        
        coh = (operators['rho']*operators['Sz']).tr().real 
        
        return coh, rho
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')



def Ramsey(operators,params,measure):
    """
    a function which constructs the Ramsey sequence using free evolution 
    and pi/2 pulses.
    Ramsey here is (U0*UX)
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        inst: bool to determine whether pulses are instantaneous. Default is False
        
    returns
    -------

    U: Qobj for the Ramsey pulse packet
    """
    
    tau = params['tau'];
    profile = params['pulse_profile']

    if params['decoherence'] == False:
        
        U0 = (-1j*operators['H0']*tau).expm();
        
            
        #construct the pulse operators
        UX, UY = pulse_profiles[profile](operators,params,rot = np.pi/2)
                
    
        U = UX*U0*UX
        
        
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    elif params['decoherence'] == False:
        raise Exception('Decoherence has not been initialised with this pulse protocol.')
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
        

def PMC(operators,params,measure,drive_dir = 'x'):
    """
    This is a function which performs PCM (phase modulated control), a Continuous 
    driving control method which modulates the phase of a second MW to engineer
    interactions
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        measure: str of which direction to measure NV
        drive_dir: str for which direction to drive NV. Default = 'x'
        
    returns
    -------
    
        coh: float value of measure NV coherence, in direction {measure}
        rho: Qobj of the final state of the system
        U: Qobj for the Ramsey pulse packet
    """
    
    tau = params['tau'];

    if params['decoherence'] == False:
        
        
        Up = (-1j*(operators['H0'] + (params['Omega_R'] + np.exp(-1j*0)*params['Omega'])*operators[f'S{drive_dir}'])*tau/2).expm()
        Um = (-1j*(operators['H0'] + (params['Omega_R'] + np.exp(-1j*np.pi)*params['Omega'])*operators[f'S{drive_dir}'])*tau).expm()
        
        U = (Up*Um*Up)**params['Np']
        
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    elif params['decoherence'] == False:
        raise Exception('Decoherence has not been initialised with this pulse protocol.')



def COSY(operators,params,measure,drive_dir = 'z'):
    """
    This is a function which performs COSY (phase modulated control), a pulsed 
    correlation method which separates two Hahn echos with tc
    
    Parameters
    ----------
    
        operators: a dict of operators for the system which can be retrieved using the 
                generate operators function
        params: dict of system parameters which define the protocol. Can be found 
                using the params() function
        measure: str of which direction to measure NV
        drive_dir: str for which direction to drive NV. Default = 'x'
        
    returns
    -------
    
        coh: float value of measure NV coherence, in direction {measure}
        rho: Qobj of the final state of the system
        U: Qobj for the Ramsey pulse packet
    """

    tau = params['tau'];
    tc = params['t_corr']
    profile = params['pulse_profile']

    if params['decoherence'] == False:
        
        U0 = (-1j*operators['H0']*tau).expm();
        U0c = (-1j*operators['H0']*tc).expm();
        
        #construct the pulse operators
        UX, UY = pulse_profiles[profile](operators,params,rot = np.pi/2)
     
        UH = UX*U0*UY*UY*U0*UY
        
        U = (UH*U0c*UH)**params['Np']
        
        rho = U*operators['rho0']*U.dag();
        
        coh = (operators['S%s'%measure]*rho).tr().real
        
    
        return coh,rho, U
    
    elif params['decoherence'] == False:
        raise Exception('Decoherence has not been initialised with this pulse protocol.')



"""
NV SYSTEM EVOLUTION
"""


def pulse_NV(operators,params,measure = 'x'):
    
    """
    a function which constructs the evolved density matrix and the coherence of the NV 
    after a particular protocol
    
    Parameters
    ----------
    
        operators: dict of quantum objects found using the generate_operators() function
        params: dict of system and protocol parameters, found using the params() function
        inst: bool to determine whether pulses are instantaneous. default = True
        
        
    returns
    -------
    
        rho: QObj for the final state of the system
        coh: float for the final coherence of the NV
    """
    
    #Np = params['Np'];
    protocol = params['protocol']
    
    protocols_dict = {'PulsePol':PulsePol,
                      'PulsePol_cam':PulsePol_cam,
                      'CPMG':CPMG,
                      'XY8':XY8,
                      'Free':Free,
                      'spin_locking':spin_locking,
                      'Ramsey': Ramsey,
                      'PMC': PMC};
    
    
    
    #U = protocols_dict[protocol](operators,params)**Np;
    
    #rho = U*operators['rho0']*U.dag();
    
    #coh = (operators['S%s'%measure]*rho).tr().real
        
    if params['decoherence'] == True:
        coh, rho = protocols_dict[protocol](operators,params,measure);
    elif params['decoherence'] == False:
        coh, rho, U = protocols_dict[protocol](operators,params,measure);
        
    else: raise Exception('Invalid value for params["decoherence"]. Must be bool not {params["decoherence"]}.')
       
        
    
    return coh, rho, U



def hyperpol(operators,params,pbar = True, re_ini = True,wait = False,random_seed2 = 1,measure ='z'):
    
    """
    A function which an initial density matrix of rho0 and applys Np pulses of a pulse scheme protocol 
    using inputed free evolution U0 and X/Y pulses UX/Y. The NV is then re-initialised and the protocol repeated. 
    the list of polarisations for each nuclear spin is returned as well as the final density matrix.
    
    Parameters
    ----------
        operators: dict of operators of the system found by using function generate_operators()
        params: dict of parameters set by using function params()
        inst: bool for whether pulses are instantaneous. default = False
        re_ini: bool for whether to re-initialise the NV. 
        
    Returns
    -------
        rho: Qobj for the final state of the system.
        Pol_array: numpy array of Pol array size N_nuc and length Reps 
    """
    
    #compute the number of nuclei in the system
    N_nuc = params['N_nuc'];
    Np = params['Np']
    protocol = params['protocol'];
    Reps = params['Reps']
    
    mu = params['t_wait_mu'];
    sigma = params['t_wait_sig']

    
    Retain = [int(x) for x in range(1,N_nuc + 1)]
    
    rho0NV = operators['rho0NV'];
    

    #compute the evolution operator for one pulse packet
    protocols_dict = {'PulsePol':PulsePol,'CPMG':CPMG,'PulsePol_cam':PulsePol_cam};
    if params['decoherence'] == False:
        coh, rho, U = protocols_dict[protocol](operators,params,measure = measure)
    else: raise Exception('This decoherence value is not supported yet.')
    
    np.random.seed(int(random_seed2))
    a = -1.46*np.log(np.random.random(Reps))*1e-6
    
    Pol_array = [];
    for i in range(N_nuc):
        Pol_array.append([]);

    if pbar == True:
        #propagate the initial matrix and find the evolution of the nuclear spin evolution
        rho = operators['rho0']
        for i in tqdm(range(Reps)):
                
        
            rho = U*rho*U.dag();
            

            #any wait time after re-initialisation
            if wait == True:
                #params['t_wait'] = random.normal(mu,sigma);
                params['t_wait'] = 10e-6

                if a[i] > 10e-6:
                    a[i] = 10e-6
                    
                #a[i] = 6e-6
                t_wait = params['t_wait'];
                
                h0 = params['omegaL']*operators['Iz'][0]
                
                U_wait = (-1j*h0*(t_wait - a[i])).expm()
                rho = U_wait*rho*U_wait.dag()
                
                #re-initiailse the NV
                rho = qutip.tensor(rho0NV,rho.ptrace(Retain))
                
                U_wait = (-1j*h0*(a[i])).expm()
                rho = U_wait*rho*U_wait.dag()
                
            else:
                #re-initiailse the NV
                rho = qutip.tensor(rho0NV,rho.ptrace(Retain))
                
            #calculate the polarisation
            for j in range(N_nuc):
                rhoTr = rho.ptrace([j + 1])
                if rhoTr.shape[0] == 2:
                    Ptemp = (2*Iz()*rhoTr).tr().real;
                    Pol_array[j].append(Ptemp);
                    
                elif rhoTr.shape[0] == 3:
                    Ptemp = (2*state_3_Sz()*rhoTr).tr().real;
                    Pol_array[j].append(Ptemp);
                  
                    
                
            

     
        
            
     
    elif pbar == False:
        #propagate the initial matrix and find the evolution of the nuclear spin evolution
        rho = operators['rho0']
        for i in range(Reps):
            
           
        
            rho = U*rho*U.dag();
            

            
            
            #any wait time after re-initialisation
            
            if wait == True:
                #params['t_wait'] = random.normal(mu,sigma);
                params['t_wait'] = 10e-6

                if a[i] > 10e-6:
                    a[i] = 10e-6
                t_wait = params['t_wait'];
                
                #a[i] = 6e-6
                h0 = params['omegaL']*operators['Iz'][0]
                U_wait = (-1j*h0*(t_wait - a[i])).expm()
                rho = U_wait*rho*U_wait.dag()
                
                #re-initiailse the NV
                rho = qutip.tensor(rho0NV,rho.ptrace(Retain))
                
                U_wait = (-1j*h0*(a[i])).expm()
                rho = U_wait*rho*U_wait.dag()
                
            else:
                #re-initiailse the NV
                rho = qutip.tensor(rho0NV,rho.ptrace(Retain))
                
            #calculate the polarisation
            for j in range(N_nuc):
                rhoTr = rho.ptrace([j + 1])
                if rhoTr.shape[0] == 2:
                    Ptemp = (2*Iz()*rhoTr).tr().real;
                    Pol_array[j].append(Ptemp);
                    
                elif rhoTr.shape[0] == 3:
                    Ptemp = (2*state_3_Sz()*rhoTr).tr().real;
                    Pol_array[j].append(Ptemp);

            

            
        
    
    return rho, Pol_array



def hyperpol_avg(operators,params, pbar = True,random_seed = 1):
    
    
    """
    A function which an initial density matrix of rho0 and applys Np pulses of a pulse scheme protocol 
    using inputed free evolution U0 and X/Y pulses UX/Y. The NV is then re-initialised and the protocol repeated. 
    the list of polarisations for each nuclear spin is returned as well as the final density matrix.
    
    Parameters
    ----------
        operators: dict of operators of the system found by using function generate_operators()
        params: dict of parameters set by using function params()
        num_avg: int for the number of t_waits averaged over. default = 100
        inst: bool for whether pulses are instantaneous. default = False
        pbar: bool for whether to include progress bar. default = True
        
    Returns
    -------
        rho: Qobj for the final state of the system.
        Pol_array: numpy array of Pol array size N_nuc and length Reps 
    """

    num_avg = params['num_avg']
    np.random.seed(random_seed)
    seeds = np.floor(np.random.random(num_avg)*100)
    
    
    if pbar == True:
        Pol_array = 0
        for i in pb.progressbar(range(num_avg)):
            
            
            rho,Pol = hyperpol(operators,params,pbar = False, wait = True,random_seed2 = seeds[i])
            Pol_array += np.array(Pol);
            
    if pbar == False:
        Pol_array = 0
        for i in range(num_avg):
            
            
            rho,Pol = hyperpol(operators,params,pbar = False,wait = True,random_seed2 = seeds[i])
            Pol_array += np.array(Pol);
                
            
    return rho,Pol_array/num_avg
        

"""
PLOTTING FUNCTIONS
"""


def plot_D_pol(P_df,fig_size = [7,4],dpi = 100,fig = None, ax = None, plot_avg = True,title = None,plot_params = plot_params(),label = None):
    
    """
    A function which plots the polarisation time series of nuclear spins under repeated
    NV polarisation
    
    Parameters
    ----------
    
    P_df: dataframe containing all the polarisation series of the nuclear spins
    plot_avg: bool which determines whether average polarisation should be plotted
    title: str which will be displayed as a title
    
    
    Returns
    --------
    
    fig: matplotlib object which conatains the plot for the figure
    
    """
    
    rc = {"font.family" : "serif", 
          "mathtext.fontset" : "stix"}
    plt.rcParams.update(rc)
    plt.rcParams["font.serif"] = ["Helvectica"] + plt.rcParams["font.serif"]

    


    
    if plot_avg == True:
        P_df['avg'] = P_df.mean(axis = 1);
    
    
    
    if fig == None or ax == None:
        
        fig = plt.figure(figsize = fig_size,dpi = dpi);
        
        ax = fig.add_subplot(1,1,1);

        mpl.rcParams['xtick.color'] = plot_params['tick_color'];
        mpl.rcParams['ytick.color'] = plot_params['tick_color'];
    
        fig.set_facecolor(plot_params['background_color'])
        ax.patch.set_facecolor(plot_params['background_color'])
    
        ax.tick_params(which = 'minor', length = 2)
        ax.tick_params(which = 'major', length = 4,labelsize = 16)

        ax.grid(ls = 'dotted',lw = 0.5,color = 'gray',zorder = 1)

 


        ax.set_ylabel('Polarisation',
                      fontsize = 16,
                      color = plot_params['text_color'])
    
        ax.set_xlabel(r'$T$ ($\mu$s)',
                      fontsize = 16,
                      color = plot_params['text_color'])
        
            
        ax.set_ylim(0,1)
    
    if title != None:
        fig.text(0.15,0.9,title,
                 fontsize = 16,fontweight = 'bold',
                 color = plot_params['text_color'])

    
    for column in P_df.columns:

            

        if column == 'avg':
            ax.plot(P_df.index,P_df[column],
                    linestyle = plot_params['line_style'],
                    label = label,
                    alpha = plot_params['line_alpha'],
                    linewidth = plot_params['line_width'],
                    color = plot_params['line_color'])
            
        else:
            ax.plot(P_df.index,P_df[column],
                    linestyle = plot_params['line_style'],
                    label = label,
                    alpha = plot_params['line_alpha'],
                    linewidth = plot_params['line_width'],
                   color = plot_params['line_color'])
    
    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    
    ax.legend(loc = 'lower right',fontsize = 12)
    
    
    return fig,ax

def plot_D_pol_N(P_df,fig_size = [7,4],fig = None, ax = None, plot_avg = True,title = None,plot_params = plot_params(),dpi = 100):
    
    """
    A function which plots the polarisation time series of nuclear spins under repeated
    NV polarisation
    
    Parameters
    ----------
    
    P_df: dataframe containing all the polarisation series of the nuclear spins
    plot_avg: bool which determines whether average polarisation should be plotted
    title: str which will be displayed as a title
    
    
    Returns
    --------
    
    fig: matplotlib object which conatains the plot for the figure
    
    """
    
    
    if plot_avg == True:
        P_df['avg'] = P_df.mean(axis = 1);
    
    
    
    if fig == None or ax == None:
        
        fig = plt.figure(figsize = fig_size,dpi = dpi);
        
        ax = fig.add_subplot(1,1,1);

        mpl.rcParams['xtick.color'] = plot_params['tick_color'];
        mpl.rcParams['ytick.color'] = plot_params['tick_color'];
    
        fig.set_facecolor(plot_params['background_color'])
        ax.patch.set_facecolor(plot_params['background_color'])
    
        ax.tick_params(which = 'minor', length = 2)
        ax.tick_params(which = 'major', length = 4,labelsize = 16)

        ax.grid(ls = 'dotted',lw = 0.5,color = 'gray',zorder = 1)

 


        ax.set_ylabel('Polarisation',
                      fontsize = 16,
                      color = plot_params['text_color'])
    
        ax.set_xlabel(r'$2\tau$ ($\mu$s)',
                      fontsize = 16,
                      color = plot_params['text_color'])
        
            
        ax.set_ylim(0,0.5)
    
    if title != None:
        fig.text(0.15,0.9,title,
                 fontsize = 16,fontweight = 'bold',
                 color = plot_params['text_color'])

    
    for column in P_df.columns:

        if column == 'avg':
            ax.plot(P_df.index,P_df[column]/2,
                    linestyle = plot_params['line_style'],
                    label = '%s'%column,
                    linewidth = 2)
            
        else:
            ax.plot(P_df.index,P_df[column]/2,
                    linestyle = plot_params['line_style'],
                    label = '%s'%column,
                    linewidth = 2)
    
    ax.legend(loc = 'lower right',fontsize = 12)
    
    
    return fig,ax
        
"""
FLOQUET
"""
    
def floquet_spectrum(operators,params,taus, bound = 1,tan2 = False,inst = True):
        
    """
    A function which takes the free Hamiltonian of a system and a partiuclar pulse
    protocol structure and finds the Floquet phase structure over a range of tau
    
    Parameters
    ----------
        operators: dict of operators for system constructed using generate_operators()
                function
        params: dict of parameters for protocol and system found by using function
                params()
        taus: array of float points which describe the range of tau for floquet spectrum
        
        
    Returns
    -------
        rho: Qobj for the final state of the system.
        Pol_array: numpy array of Pol array size N_nuc and length Reps 
    """
    protocols_dict = {'PulsePol':PulsePol,'CPMG':CPMG};
    
    #retrieve protocol parameters
    N_nuc = params['N_nuc'];
    protocol = params['protocol']
    
    
    ''' find the unperturbed starting floquet states '''
    params['tau'] = 1e-9;
    
    U_ini =  protocols_dict[protocol](operators,params,inst);
    lbda, vecOld = U_ini.eigenstates(sort = 'low');
    
    
    
    
    ''' initialise arrays '''
    E = []
    Vec = []
    wind = [];
    for i in range(2**(N_nuc + 1)):
        
        E.append([]);
        Vec.append([])
        wind.append(0);

    ''' run through tau array and find all floquet phases and states '''   
    for j in pb.progressbar(range(len(taus))):
        
        states = []
        params['tau'] = taus[j]
        

        U = protocols_dict[protocol](operators,params,inst);
        
        lbda,vectemp = U.eigenstates(sort = 'low');
        
        if tan2 == True:
            #convert into floquet phases
            etemp = np.arctan2(lbda.imag,lbda.real)
            f = 1/2
        elif tan2 == False:
            #convert into floquet phases
            etemp = np.arctan(lbda.imag/lbda.real)
            f = 1
        
        etemp = np.array(etemp)
        
        
        idx = np.argsort(etemp);
        etemp = etemp[idx]    
        vectemp = vectemp[idx]
        #assign the correct floquet state to the correct array to prevent discontinuities
        for i in range(len(etemp)):

            overlapMax = 0

            for k in range(len(vecOld)):
                overlap = abs((vectemp[i].overlap(vecOld[k])))**2

                if overlap > overlapMax and k not in states:
                    state = k;
                    overlapMax = overlap;

            states.append(state)


            #assign winding number for states to remove discontinuities due to oscillatory wrapping
            if j > 0:
                if E[state][-1] - etemp[i] - 2*f*np.pi*wind[state] > np.pi/2*f:

                    wind[state] +=1;

                elif E[state][-1] - etemp[i] - 2*f*np.pi*wind[state] < -np.pi/2*f:

                    wind[state] -=1;

            E[state].append(etemp[i] + 2*f*np.pi*wind[state]);
            Vec[state].append(vectemp[i]);

        #store the new floquet states as the old floquet states for the next loop
        vecNew = [];
        for n in range(len(states)):
            vecNew.append([])
            
        for n in range(len(states)):
            vecNew[states[n]] = vectemp[n] 
        vecOld = vecNew;
        
        return E,Vec
    

    

"""
NV GENERATOR
"""


def nv_generator(params = params(),lat = [-10,10],p = 0.011,species = 'C',random_state = None):
    """
    nv_generator is a function which takes in the size of a lattice and generates 
    a random bath of species C.
    
    Parameters:
               params: a dict of parameters commonly used for NV centres. This 
                       function will use the lattice vectors
               lat: array of integers for start N_s and end N_f of the number of lattice
                   repetitions. Default = [-10,10]
               p: the probability that the lattice site is the chosen species.
               species: The label for the species of impurity. Choice between H or C
               
    returns:
            df: dataframe of Nv hyperfine couplings, positions and species label
    """

    R = params['vecs']
    sites = []
    
    np.random.seed(random_state)

    # for loop for x direction
    for n in range(lat[0],lat[1] + 1):
        #for loop for y direction
        for l in range(lat[0],lat[1] + 1):
            #for loop for z direction
            for m in range(lat[0],lat[1] + 1):
                #loop over vectors
                for vec in range(len(R)):

                    r = random.random()
                    new = np.add(R[vec], [n,l,m])
                    
                    if new[0] == 0.25 and new[1] == 0.25 and new[2] == 0.25:
                        
                        Val = new;
                        

                    elif new[0] == 0 and new[1] == 0 and new[2] == 0:

                        N14 = new;
                    

                    elif r <= p:
                        temp = np.subtract(new,[0.25,0.25,0.25]);

                       #change basis
                        temp = change_basis(temp);

                        
                        if species == 'p1':
                            #find hyperfine coupling using previously defined function
                            s = '14N' if np.random.random() < 1 else 'N'
                            A = hyperfine(temp*params['lattice_constant']*1e10,params=params,species = s)
                            Apar = A[2];
                            Aper = np.linalg.norm([A[0],A[1]]);
                            sites.append([s,A[0],A[1],A[2],Apar,Aper,(temp*params['lattice_constant']*1e10).round(2)])
                            #find hyperfine coupling using previously defined function
                            
                            A = hyperfine(temp*params['lattice_constant']*1e10,params=params,species = 'e')
                            Apar = A[2];
                            Aper = np.linalg.norm([A[0],A[1]]);
                            sites.append(['p1',A[0],A[1],A[2],Apar,Aper,(temp*params['lattice_constant']*1e10).round(2)])
                        else:
                            #find hyperfine coupling using previously defined function
                            A = hyperfine(temp*params['lattice_constant']*1e10,params=params,species = species)
                            Apar = A[2];
                            Aper = np.linalg.norm([A[0],A[1]]);

                        
                        
                            sites.append([species,A[0],A[1],A[2],Apar,Aper,(temp*params['lattice_constant']*1e10).round(2)])
                        
    df = pd.DataFrame(sites,columns = ['Species','Ax','Ay','Az','Apar','Aper','pos'])




    return df

    