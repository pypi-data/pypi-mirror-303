#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:59:20 2022

@author: ollywhaites
"""
import sys
sys.path.insert(1,'/Users/ollywhaites/Documents/Documents/PhD/Python/Libraries')

import numpy as np
import pandas as pd
import NV_Library as nv
from tqdm import tqdm

from os import path

"""
libraries functions
"""


def PCE2(spins,centre_spin,couplings,taus,params = nv.params(),pbar = True,avg = False,CC_coupling = False,dataset = ''):
    
    """
    A program which finds PCE for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                centre_spin: int of PCE spin of interest
                couplings: dataframe of couplings Ax, Az for each spin in bath
                taus: array of taus for tau sweep
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                avg: bool for whether a t_wait average is needed
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    params['N_nuc'] = 2
    operators, params = nv.generate_operators([0,0], [0,0], params)


    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Polarise_bath/PCE/data/%s_data/2_spin/'%dataset


    # PCE4 = pd.DataFrame(columns = ['P3'], index = taus*1e6)
    if avg == True:
        filename = 'done_wait.csv'
    else: filename = 'done.csv'
    
        
    if path.exists(Dir + filename):
        done = pd.read_csv(Dir + filename,index_col = 0).values.tolist()
    else: 
        done = []

    
    

    if pbar == True:
    
        for s in tqdm(spins,desc = 'PCE2, Spin {}: '.format(centre_spin),position = 0):
            
            if s != centre_spin:
    
                    lst = [centre_spin,s];
                    lst.sort()
                    print(lst)
                    lst.append(params['Reps'])
                    lst.append(params['Np'])
                    if avg == True:
                        lst.append(params['num_avg'])
                        
                    lst.append(CC_coupling)
                    if lst not in done:
                        # operators = nv.generate_H0(operators,
                        #                            [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s]],
                        #                            [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s]],
                        #                            params)
                        operators = nv.generate_full_H0(operators,
                                                     couplings = couplings.loc[[centre_spin,s]],
                                                     params = params,
                                                     CC_coupling = CC_coupling)
                        
                        P2 = []
                        for t in taus:
                            params['tau'] = t;
                            
                            if avg == True:
                                rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                            else:
                                rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                            
                            P2.append(np.array(Ptemp).T[-1])
                        
                        # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                        sub_sys = [centre_spin,s]
                        PCE2_all = pd.DataFrame(P2,columns = sub_sys,index = taus*1e6)
                        sub_sys.sort()
                        
                        filename_PCE = '{}_C{}_C{}_R{}_Np{}'.format(params['protocol'],sub_sys[0],sub_sys[1],params['Reps'],params['Np'])
                
                        if avg == True:
                            filename_PCE = filename_PCE +  '_wait{}'.format(params['num_avg'])
                        if CC_coupling == True:
                            filename_PCE = filename_PCE +  '_full'
                        filename_PCE = filename_PCE + '.csv'   
                        
                        PCE2_all.to_csv(Dir + filename_PCE)

                        done.append(lst);
                        
    else:

        for s in spins:
            
            if s != centre_spin:
    
                    lst = [centre_spin,s];
                    lst.sort()
                    print(lst)
                    lst.append(params['Reps'])
                    lst.append(params['Np'])
                    if avg == True:
                        lst.append(params['num_avg'])
                        
                    lst.append(CC_coupling)
                    if lst not in done:
                        # operators = nv.generate_H0(operators,
                        #                            [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s]],
                        #                            [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s]],
                        #                            params)
                        operators = nv.generate_full_H0(operators,
                                                     couplings = couplings.loc[[centre_spin,s]],
                                                     params = params,
                                                     CC_coupling = CC_coupling)
                        P2 = []
                        for t in taus:
                            params['tau'] = t;
                            if avg == True:
                                rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                            else:
                                rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                            P2.append(np.array(Ptemp).T[-1])
                        
                        # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                        sub_sys = [centre_spin,s]
                        PCE2_all = pd.DataFrame(P2,columns = sub_sys,index = taus*1e6)
                        sub_sys.sort()
                
                        filename_PCE = '{}_C{}_C{}_R{}_Np{}'.format(params['protocol'],sub_sys[0],sub_sys[1],params['Reps'],params['Np'])
                
                        if avg == True:
                            filename_PCE = filename_PCE +  '_wait{}'.format(params['num_avg'])
                        if CC_coupling == True:
                            filename_PCE = filename_PCE + '_full'
                        filename_PCE = filename_PCE + '.csv'    
                        
                        PCE2_all.to_csv(Dir + filename_PCE)
                        
                    
                        done.append(lst);
    columns = ['s1','s2','Reps','Np']
    if avg == True:
        columns.append('num_avg')
        
    columns.append('full')

    done_df = pd.DataFrame(done,columns = columns)
    done_df.to_csv(Dir + filename)
    
    return done_df




def PCE3(spins,centre_spin,couplings,taus,params = nv.params(),pbar = True,avg = False,CC_coupling = False,dataset = ''):
    
    """
    A program which finds PCE for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                centre_spin: int of PCE spin of interest
                couplings: dataframe of couplings Ax, Az for each spin in bath
                taus: array of taus for tau sweep
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                avg: bool for whether a t_wait average is needed
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    params['N_nuc'] = 3
    operators, params = nv.generate_operators([0,0,0], [0,0,0], params)


    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Polarise_bath/PCE/data/%s_data/3_spin/'%dataset


    # PCE4 = pd.DataFrame(columns = ['P3'], index = taus*1e6)
    if avg == True:
        filename = 'done_wait.csv'
    else: filename = 'done.csv'
    
        
    if path.exists(Dir + filename):
        done = pd.read_csv(Dir + filename,index_col = 0).values.tolist()
        
    else: done = []
    
    

    if pbar == True:
    
        
        for s in tqdm(spins,desc = 'PCE3, Spin {}: '.format(centre_spin),position = 0):
            if s != centre_spin:
                for p in tqdm(spins,desc = '2nd Spin {}: '.format(s),position = 1):
                        lst = [centre_spin,s,p];
                        lst.sort()
                        lst.append(params['Reps'])
                        lst.append(params['Np'])
                        if avg == True:
                            lst.append(params['num_avg'])
                            
                        lst.append(CC_coupling)

                        if p != centre_spin and p != s and lst not in done:
                            # operators = nv.generate_H0(operators,
                            #                            [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s],couplings['Az'].loc[p]],
                            #                            [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s],couplings['Ax'].loc[p]],
                            #                            params)
                            operators = nv.generate_full_H0(operators,
                                                         couplings = couplings.loc[[centre_spin,s,p]],
                                                         params = params,
                                                         CC_coupling = CC_coupling)
                            P3 = []
                            for t in taus:
                                params['tau'] = t;
                                if avg == True:
                                    rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                                else:
                                    rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                                P3.append(np.array(Ptemp).T[-1])
                            
                            # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                            sub_sys = [centre_spin,s,p]

                            PCE3_all = pd.DataFrame(P3,columns = sub_sys,index = taus*1e6)
                            sub_sys.sort()

                            filename_PCE = '{}_C{}_C{}_C{}_R{}_Np{}'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],params['Reps'],params['Np'])
                    
                            if avg == True:
                                filename_PCE = filename_PCE +  '_wait{}'.format(params['num_avg'])
                            if CC_coupling == True:
                                filename_PCE = filename_PCE + '_full'
                            filename_PCE = filename_PCE + '.csv'    
                            PCE3_all.to_csv(Dir + filename_PCE)
                        
                            done.append(lst);
                            
    else:

        for s in spins:
            if s != centre_spin:
                for p in spins:
                        lst = [centre_spin,s,p];
                        lst.sort()
                        lst.append(params['Reps'])
                        lst.append(params['Np'])
                        if avg == True:
                            lst.append(params['num_avg'])
                            
                        lst.append(CC_coupling)

                        if p != centre_spin and p != s and lst not in done:
                            # operators = nv.generate_H0(operators,
                            #                            [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s],couplings['Az'].loc[p]],
                            #                            [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s],couplings['Ax'].loc[p]],
                            #                            params)
                            operators = nv.generate_full_H0(operators,
                                                         couplings = couplings.loc[[centre_spin,s,p]],
                                                         params = params,
                                                         CC_coupling = CC_coupling)
                            
                            P3 = []
                            for t in taus:
                                params['tau'] = t;
                                if avg == True:
                                    rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                                else:
                                    rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                                P3.append(np.array(Ptemp).T[-1])
                            
                            # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                            sub_sys = [centre_spin,s,p]

                            PCE3_all = pd.DataFrame(P3,columns = sub_sys,index = taus*1e6)
                            sub_sys.sort()

                            filename_PCE = '{}_C{}_C{}_C{}_R{}_Np{}'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],params['Reps'],params['Np'])
                    
                            if avg == True:
                                filename_PCE = filename_PCE +  '_wait{}'.format(params['num_avg'])
                            if CC_coupling == True:
                                filename_PCE = filename_PCE + '_full'
                            filename_PCE = filename_PCE + '.csv'  
                            PCE3_all.to_csv(Dir + filename_PCE)
                        
                            done.append(lst);

    columns = ['s1','s2','s3','Reps','Np']
    if avg == True:
        columns.append('num_avg')
        
    columns.append('full')

    done_df = pd.DataFrame(done,columns = columns)
    done_df.to_csv(Dir + filename)
    
    return done_df


def PCE4(spins,centre_spin,couplings,taus,params = nv.params(),pbar = True,avg = False,CC_coupling = False,dataset = ''):
    
    """
    A program which finds PCE 4for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                centre_spin: int of PCE spin of interest
                couplings: dataframe of couplings Ax, Az for each spin in bath
                taus: array of taus for tau sweep
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                avg: bool for whether a t_wait average is needed
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    params['N_nuc'] = 4
    operators, params = nv.generate_operators([0,0,0,0], [0,0,0,0], params)


    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Polarise_bath/PCE/data/%s_data/4_spin/'%dataset


    # PCE4 = pd.DataFrame(columns = ['P3'], index = taus*1e6)
    if avg == True:
        filename = 'done_wait.csv'
    else: filename = 'done.csv'
    
        
    if path.exists(Dir + filename):
        done = pd.read_csv(Dir + filename,index_col = 0).values.tolist()
        
    else: done = []
    
    

    if pbar == True:
    
        
        for s in tqdm(spins,desc = 'PCE4, Spin {}: '.format(centre_spin),position = 0):
            if s != centre_spin:
                for p in tqdm(spins,desc = '2nd Spin {}: '.format(s),position = 1):
                    if p != centre_spin and p != s:
                        for q in tqdm(spins,desc = '3rd Spin {}: '.format(p),position = 2):
                            lst = [centre_spin,s,p,q];
                            lst.sort()
                            lst.append(params['Reps'])
                            lst.append(params['Np'])
                            if avg == True:
                                lst.append(params['num_avg'])
                                
                            lst.append(CC_coupling)
                            if q != centre_spin and q != s and q != p and lst not in done:
                                # operators = nv.generate_H0(operators,
                                #                            [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s],couplings['Az'].loc[p],couplings['Az'].loc[q]],
                                #                            [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s],couplings['Ax'].loc[p],couplings['Ax'].loc[q]],
                                #                            params)
                                operators = nv.generate_full_H0(operators,
                                                             couplings = couplings.loc[[centre_spin,s,p,q]],
                                                             params = params,
                                                             CC_coupling = CC_coupling)
                                
                                P4 = []
                                for t in taus:
                                    params['tau'] = t;
                                    if avg == True:
                                        rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                                    else:
                                        rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                                    P4.append(np.array(Ptemp).T[-1])
                                
                                # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                                sub_sys = [centre_spin,s,p,q]

                                PCE4_all = pd.DataFrame(P4,columns = sub_sys,index = taus*1e6)
                                sub_sys.sort()
                                filename_PCE = '{}_C{}_C{}_C{}_C{}_R{}_Np{}'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],sub_sys[3],params['Reps'],params['Np'])
                        
                                if avg == True:
                                    filename_PCE = filename_PCE +  '_wait{}'.format(params['num_avg'])
                                if CC_coupling == True:
                                    filename_PCE = filename_PCE + '_full'
                                filename_PCE = filename_PCE + '.csv'  
                                PCE4_all.to_csv(Dir + filename_PCE)

                                done.append(lst);
                            
    else:

        for s in spins:
            if s != centre_spin:
                for p in tqdm(spins,desc = '2nd Spin {}: '.format(s),position = 1):
                    if p != centre_spin and p != s:
                        for q in tqdm(spins,desc = '3rd Spin {}: '.format(p),position = 2):
                            lst = [centre_spin,s,p,q];
                            lst.sort()
                            lst.append(params['Reps'])
                            lst.append(params['Np'])
                            if avg == True:
                                lst.append(params['num_avg'])
                                
                            lst.append(CC_coupling)
                            if q != centre_spin and q != s and q != p and lst not in done:
                                # operators = nv.generate_H0(operators,
                                #                            [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s],couplings['Az'].loc[p],couplings['Az'].loc[q]],
                                #                            [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s],couplings['Ax'].loc[p],couplings['Ax'].loc[q]],
                                #                            params)
                                operators = nv.generate_full_H0(operators,
                                                             couplings = couplings.loc[[centre_spin,s,p,q]],
                                                             params = params,
                                                             CC_coupling = CC_coupling)
                                P4 = []
                                for t in taus:
                                    params['tau'] = t;
                                    if avg == True:
                                        rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                                    else:
                                        rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                                    P4.append(np.array(Ptemp).T[-1])
                                
                                # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                                sub_sys = [centre_spin,s,p,q]

                                PCE4_all = pd.DataFrame(P4,columns = sub_sys,index = taus*1e6)
                                sub_sys.sort()
                                filename_PCE = '{}_C{}_C{}_C{}_C{}_R{}_Np{}'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],sub_sys[3],params['Reps'],params['Np'])
                        
                                if avg == True:
                                    filename_PCE = filename_PCE +  '_wait{}'.format(params['num_avg'])
                                if CC_coupling == True:
                                    filename_PCE = filename_PCE + '_full'
                                filename_PCE = filename_PCE + '.csv' 
                                PCE4_all.to_csv(Dir + filename_PCE)

                                done.append(lst);

    columns = ['s1','s2','s3','s4','Reps','Np']
    if avg == True:
        columns.append('num_avg')
        
    columns.append('full')

    done_df = pd.DataFrame(done,columns = columns)
    done_df.to_csv(Dir + filename)
    
    return done_df

def PCE5(spins,centre_spin,couplings,taus,params = nv.params(),pbar = True,avg = False):
    
    """
    A program which finds PCE 4for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                centre_spin: int of PCE spin of interest
                couplings: dataframe of couplings Ax, Az for each spin in bath
                taus: array of taus for tau sweep
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                avg: bool for whether a t_wait average is needed
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    params['N_nuc'] = 5
    operators, params = nv.generate_operators([0,0,0,0,0], [0,0,0,0,0], params)


    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Polarise_bath/PCE/data/toy_data/5_spin/'


    # PCE4 = pd.DataFrame(columns = ['P3'], index = taus*1e6)
    if avg == True:
        filename = 'done_wait.csv'
    else: filename = 'done.csv'
    
        
    if path.exists(Dir + filename):
        done = pd.read_csv(Dir + filename,index_col = 0).values.tolist()
        
    else: done = []
    
    

    if pbar == True:
    
        
        for s in tqdm(spins,desc = 'PCE5, Spin {}: '.format(centre_spin),position = 0):
            if s != centre_spin:
                for p in tqdm(spins,desc = '2nd Spin {}: '.format(s),position = 1):
                    if p != centre_spin and p != s:
                        for q in tqdm(spins,desc = '3nd Spin {}: '.format(p),position = 1):
                            if q != centre_spin and q != s and q != p:
                                for r in tqdm(spins,desc = '4rd Spin {}: '.format(q),position = 2):
                                    lst = [centre_spin,s,p,q,r];
                                    lst.sort()
                                    lst.append(params['Reps'])
                                    if avg == True:
                                        lst.append(params['num_avg'])
                                    if r != centre_spin and r != s and r != p and r != q and lst not in done:
                                        operators = nv.generate_H0(operators,
                                                                   [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s],couplings['Az'].loc[p],couplings['Az'].loc[q],couplings['Az'].loc[r]],
                                                                   [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s],couplings['Ax'].loc[p],couplings['Ax'].loc[q],couplings['Ax'].loc[r]],
                                                                   params)
                                        P5 = []
                                        for t in taus:
                                            params['tau'] = t;
                                            if avg == True:
                                                rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                                            else:
                                                rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                                            P5.append(np.array(Ptemp).T[-1])
                                        
                                        # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                                        sub_sys = [centre_spin,s,p,q,r]
        
                                        PCE5_all = pd.DataFrame(P5,columns = sub_sys,index = taus*1e6)
                                        sub_sys.sort()
                                        if avg == True:
                                            filename_PCE = '{}_C{}_C{}_C{}_C{}_C{}_R{}_Np{}_wait{}.csv'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],sub_sys[3],sub_sys[4],params['Reps'],params['Np'],params['num_avg'])
                                        else:
                                            filename_PCE = '{}_C{}_C{}_C{}_C{}_C{}_R{}_Np{}.csv'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],sub_sys[3],sub_sys[4],params['Reps'],params['Np'])
                                        PCE5_all.to_csv(Dir + filename_PCE)
        
                                        done.append(lst);
                            
    else:

        for s in spins:
            if s != centre_spin:
                for p in tqdm(spins,desc = '2nd Spin {}: '.format(s),position = 1):
                    if p != centre_spin and p != s:
                        for q in tqdm(spins,desc = '3nd Spin {}: '.format(p),position = 1):
                            if q != centre_spin and q != s and q != p:
                                for r in tqdm(spins,desc = '4rd Spin {}: '.format(q),position = 2):
                                    lst = [centre_spin,s,p,q,r];
                                    lst.sort()
                                    lst.append(params['Reps'])
                                    if avg == True:
                                        lst.append(params['num_avg'])
                                    if r != centre_spin and r != s and r != p and r != q and lst not in done:
                                        operators = nv.generate_H0(operators,
                                                                   [couplings['Az'].loc[centre_spin],couplings['Az'].loc[s],couplings['Az'].loc[p],couplings['Az'].loc[q],couplings['Az'].loc[r]],
                                                                   [couplings['Ax'].loc[centre_spin],couplings['Ax'].loc[s],couplings['Ax'].loc[p],couplings['Ax'].loc[q],couplings['Ax'].loc[r]],
                                                                   params)
                                        P5 = []
                                        for t in taus:
                                            params['tau'] = t;
                                            if avg == True:
                                                rho,Ptemp = nv.D_pol_avg(operators,params,pbar = False)
                                            else:
                                                rho,Ptemp = nv.D_pol(operators,params,pbar = False)
                                            P5.append(np.array(Ptemp).T[-1])
                                        
                                        # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                                        sub_sys = [centre_spin,s,p,q,r]
        
                                        PCE5_all = pd.DataFrame(P5,columns = sub_sys,index = taus*1e6)
                                        sub_sys.sort()
                                        if avg == True:
                                            filename_PCE = '{}_C{}_C{}_C{}_C{}_C{}_R{}_Np{}_wait{}.csv'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],sub_sys[3],sub_sys[4],params['Reps'],params['Np'],params['num_avg'])
                                        else:
                                            filename_PCE = '{}_C{}_C{}_C{}_C{}_C{}_R{}_Np{}.csv'.format(params['protocol'],sub_sys[0],sub_sys[1],sub_sys[2],sub_sys[3],sub_sys[4],params['Reps'],params['Np'])
                                        PCE5_all.to_csv(Dir + filename_PCE)
        
                                        done.append(lst);

    columns = ['s1','s2','s3','s4','Reps']
    if avg == True:
        columns.append('num_avg')

    done_df = pd.DataFrame(done,columns = columns)
    done_df.to_csv(Dir + filename)
    
    return done_df






