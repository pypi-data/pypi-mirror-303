#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 11:48:14 2024

@author: ollywhaites
"""
from sys import path
path.append('/Users/ollywhaites/Documents/Documents/PhD/Python/Libraries/')

import numpy as np
import NV_Library as nv


def rot_mat(a,b):
    
    R = np.array([[np.cos(a)*np.cos(b),np.cos(b)*np.sin(a),-np.sin(b)],
         [-np.sin(a),np.cos(a),0],
         [np.sin(b)*np.cos(a),np.sin(b)*np.sin(a),np.cos(b)]])

    return R
def find_axisCoup(Adiag,axis = 'D'):
    
    rot = {'A':{'a':0,'b':np.radians(109.5)},
           'B':{'a':0*np.radians(120),'b':np.radians(109.5)},
           'C':{'a':0*np.radians(240),'b':np.radians(109.5)},
           'D':{'a':0,'b':0}}
    
    R = rot_mat(rot[axis]['a'], rot[axis]['b'])
    
    return np.dot(np.dot(R,Adiag),R.T)


def tensor_prod(operators,i,j,PN):
    
    axis = {0:'x',
            1: 'y',
            2: 'z'}
    
    HQ = 0
    for n in range(3):
        #m = n
        for m in range(3):
            HQ += PN[n][m]*operators['I%s'%axis[n]][i]*operators['I%s'%axis[m]][j]
            
            
    return HQ


def construct_H0(operators,params,spins,bath,Tin):
    

    
    H0 = 0
    if params['lab'] == True:
        H0 += params['omega_e']*operators['Sz'] + params['zfs_NV']*operators['Sz']*operators['Sz'] 
    
    Hi = 0
    Hij = 0
    k = 0
    for i in spins:

        r1 = {'x':bath.loc[i].iloc[1]['pos'][0]*1e-10,
                'y':bath.loc[i].iloc[1]['pos'][1]*1e-10,
                'z':bath.loc[i].iloc[1]['pos'][2]*1e-10}
        
        
        if bath.loc[i].iloc[0]['Species'] == 'N':
            Adiag = np.array([[-2*np.pi*113.83e6,0,0],[0,-2*np.pi*113.83e6,0],[0,0,-2*np.pi*159.7e6]]) 
            Pdiag = np.array([[0,0,0],[0,0,0],[0,0,0]])
        else:

            Adiag = np.array([[2*np.pi*81.32e6,0,0],[0,2*np.pi*81.32e6,0],[0,0,2*np.pi*114.03e6]]) 
            Pdiag = np.array([[2*np.pi*1.32e6,0,0],[0,2*np.pi*1.32e6,0],[0,0,2*np.pi*2.65e6]])
            Pdiag = np.array([[2*np.pi*0,0,0],[0,2*np.pi*0,0],[0,0,-2*np.pi*3.97e6]])
            
        #AN = find_axisCoup(Adiag,axis = bath.loc[i]['JT_axis'].iloc[1])
        PN = find_axisCoup(Pdiag,axis = bath.loc[i]['JT_axis'].iloc[1])
        
        if Tin == True:
            AN = find_axisCoup(Adiag,axis = bath.loc[i]['JT_axis'].iloc[1])[2]
            
            Hi += (params['D']*operators['Iz'][2*k + 0] + 2*np.pi*params['gamma_N']*params['B0']*operators['Iz'][2*k + 1] 
                   + (AN[2]*operators['Iz'][2*k  + 1] + AN[0]*operators['Ix'][2*k  + 1] + AN[1]*operators['Iy'][2*k  + 1])*operators['Iz'][2*k + 0]
                   #+ tensor_prod(operators,2*k  + 1,2*k + 1,PN)
                   + 2*np.pi*1e3*(bath.loc[i]['Az'].iloc[1]*operators['Iz'][2*k  + 0])*operators['Sz']
                   + params['Omega_RF']*(np.sin(params['RF_phase'])*operators['Ix'][2*k  + 0] + np.cos(params['RF_phase'])*operators['Iy'][2*k  + 0]))
            
        elif Tin == False:
            AN = find_axisCoup(Adiag,axis = bath.loc[i]['JT_axis'].iloc[1])
              
            Hi += (2*np.pi*params['gamma_e']*params['B0']*operators['Iz'][2*k + 0]  + 2*np.pi*params['gamma_N']*params['B0']*operators['Iz'][2*k + 1] 
                   + tensor_prod(operators,2*k  + 0,2*k + 1,AN)
                   #+ (AN[2]*operators['Iz'][2*k  + 1] + AN[0]*operators['Ix'][2*k  + 1] + AN[1]*operators['Iy'][2*k  + 1])*operators['Iz'][2*k + 0]
                   + tensor_prod(operators,2*k  + 1,2*k + 1,PN)
                   + 2*np.pi*1e3*(bath.loc[i]['Az'].iloc[1]*operators['Iz'][2*k  + 0])*operators['Sz']
                   #+ 2*np.pi*1e3*(bath.loc[i]['Az'].iloc[1]*operators['Iz'][2*k  + 0] + bath.loc[i]['Ax'].iloc[1]*operators['Ix'][2*k  + 0] + bath.loc[i]['Ay'].iloc[1]*operators['Iy'][2*k  + 0])*operators['Sz']
                   #+ 2*params['Omega']*(np.sin(params['omega_RF']*params['t'] - params['RF_phase'])*operators['Ix'][2*k  + 0]))
                   )
            

        for j in spins[k + 1:]:

            r2 = {'x':bath.loc[j].iloc[1]['pos'][0]*1e-10,
                    'y':bath.loc[j].iloc[1]['pos'][1]*1e-10,
                    'z':bath.loc[j].iloc[1]['pos'][2]*1e-10}
            
            
            Cij = 2*np.pi*nv.cc_coupling(r1,r2,params = params,species = 'e')
            
            Hij += Cij*(operators['Iz'][2*k  + 0]*operators['Iz'][2*k + 2] - (1/2)*(operators['Ix'][2*k  + 0]*operators['Ix'][2*k + 2] + operators['Iy'][2*k  + 0]*operators['Iy'][2*k + 2]))

            
        k+=1
    operators['H0'] = H0 + Hi + Hij
    
    return operators,params


def LG4(operators,params,bath,spins,Tin):
    
    D = params['D']
    Om = params['Omega']
    alpha = params['RF_phase']
    
    operators,params = construct_H0(operators,params,spins,bath,Tin)
    rho,coh, UA = nv.pulse_NV(operators,params,measure = 'x',)
    
    params['D'] = -D
    params['Omega'] = -Om
    params['RF_phase'] = alpha
    
    operators,params = construct_H0(operators,params,spins,bath,Tin)
    rho,coh, UAm = nv.pulse_NV(operators,params,measure = 'x',)
    
    params['D'] = D
    params['Omega'] = Om
    params['RF_phase'] = -alpha
    
    operators,params = construct_H0(operators,params,spins,bath,Tin)
    rho,coh, UB = nv.pulse_NV(operators,params,measure = 'x',)
    
    
    params['D'] = -D
    params['Omega'] = -Om
    params['RF_phase'] = -alpha
    
    operators,params = construct_H0(operators,params,spins,bath,Tin)
    rho,coh, UBm = nv.pulse_NV(operators,params,measure = 'x',)
    
    params['D'] = D
    params['Omega'] = Om
    params['RF_phase'] = alpha
    
    U = UBm*UB*UAm*UA
    
    return U
    


def LG(operators,params,bath,spins,Tin):

    operators,params = construct_H0(operators,params,spins,bath,Tin)
    rho,coh, U = nv.pulse_NV(operators,params,measure = 'x',)
    
    return U

RF_protocols = {'LG': LG,
                'LG4': LG4}

def  find_U(operators,params,bath,spins,Tin):
    
    U = RF_protocols[params['RF_protocol']](operators,params,bath,spins,Tin)
    
    return U