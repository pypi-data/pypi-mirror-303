#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:32:37 2022

@author: ollywhaites
"""

"""
import modules
"""
from sys import path

path.append('/Users/ollywhaites/Documents/Documents/PhD/Python/Libraries')

import NV_Library as nv
import pandas as pd
import numpy as np
import math

from tqdm import tqdm

from os import path

"""
define functions
"""

def CCE0(spins,couplings,ts,params = nv.params(),pbar = True,NV_state = 'Xp',measure = 'x',NV_sub = '-'):
    
    """
    A program which finds PCE for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                couplings: dataframe of couplings Ax, Az for each spin in bath
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Extend_coherence/CCE/{}/data/'.format(params['protocol'])

    
    params['N_nuc'] = 0
    operators, params = nv.generate_operators([], [], params, NV_state = NV_state,NV_sub=NV_sub)
    
    operators = nv.generate_full_H0(operators,
                               couplings.loc[[]],
                               params = params,
                               CC_coupling = False)
    
    L0 = [];
    for t in ts:
        
        params['tau'] = t
        params['t_ev'] = t
        
        Ltemp, rho = nv.pulse_NV(operators,params, inst = False,measure = measure)
        L0.append(Ltemp.real)
        
    sub_sys = []
    CCE0 = pd.DataFrame(L0,columns = ['coherence'],index = ts)
    sub_sys.sort()

    filename_CCE = 'CCE0.csv'
    CCE0.to_csv(Dir + filename_CCE)
         
    

def CCE1(spins,couplings,ts,params = nv.params(),pbar = True,NV_state = 'Xp',measure = 'x',NV_sub = '-',cluster = 'test'):
    
    """
    A program which finds PCE for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                couplings: dataframe of couplings Ax, Az for each spin in bath
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    params['N_nuc'] = 1
    operators, params = nv.generate_operators([0], [0], params, NV_state = NV_state,NV_sub = NV_sub)


    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Extend_coherence/CCE/{}/{}_data/1_spin/'.format(params['protocol'],cluster)


    # PCE4 = pd.DataFrame(columns = ['P3'], index = taus*1e6)

    filename = 'done.csv'
    
        
    if path.exists(Dir + filename):
        done = pd.read_csv(Dir + filename,index_col = 0).values.tolist()
        
    else: done = []
    done = []
    

    if pbar == True:
    
        for s in tqdm(spins,desc = 'CCE1',position = 0):
        

                lst = [s];
                if lst not in done:
                    
                    
                    operators = nv.generate_full_H0(operators,
                                               couplings.loc[[s]],
                                               params = params,
                                               CC_coupling = False)
                    L1 = [];
                    for t in ts:
                        
                        params['tau'] = t
                        params['t_ev'] = t
                        
                        Ltemp, rho = nv.pulse_NV(operators,params,measure=measure)
                        L1.append(Ltemp.real)
                
                    

                    # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                    sub_sys = [s]
                    CCE1 = pd.DataFrame(L1,columns = ['coherence'],index = ts)
                    sub_sys.sort()

                    filename_CCE = 'C{}.csv'.format(sub_sys[0])
                    CCE1.to_csv(Dir + filename_CCE)
                
                    done.append(lst);
                        
    else:
    
        for s in spins:
        
                lst = [s];


                if lst not in done:
                       operators = nv.generate_full_H0(operators,
                                               couplings.loc[[s]],
                                               params = params,
                                               CC_coupling = False)

                    
                
                       L1 = [];
                       for t in ts:
                           
                           params['tau'] = t
                           params['t_ev'] = t
                           
                           Ltemp, rho = nv.pulse_NV(operators,params,measure = measure)
                           L1.append(Ltemp)
                       
                       
                       
                       # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                       sub_sys = [s]
                       CCE1 = pd.DataFrame(L1,columns = ['coherence'],index = ts)
                       sub_sys.sort()
                
                       filename_CCE = 'C{}.csv'.format(sub_sys[0])
                       CCE1.to_csv(Dir + filename_CCE)
                   
                       done.append(lst);

    done_df = pd.DataFrame(done)
    done_df.to_csv(Dir + filename)
    
    return done_df


def CCE2(spins,couplings,ts,params = nv.params(),pbar = True, NV_state = 'Xp',measure = 'x',NV_sub = '-',cluster = 'test',CC_coupling = True):
    
    """
    A program which finds PCE for a bath of spins and coupled to the NV.
    
    Parameters
    ----------
                spins: list of a spin numbers which exist in bath and couplings data frame
                couplings: dataframe of couplings Ax, Az for each spin in bath
                params: dict of parameters needed for the simulations. default
                        = nv.params() which is constructed in NV_Library library
                pbar: bool determines whether progressbar is needed. defualt =
                        True
                
                
    Returns:
    --------
                done_df: dataframe of spins which have been constructed
    """
    
    params['N_nuc'] = 2
    operators, params = nv.generate_operators([0,0], [0,0], params, NV_state = NV_state,NV_sub = NV_sub)


    Dir = '/Users/ollywhaites/Documents/Documents/PhD/Python/Extend_coherence/CCE/{}/{}_data/2_spin/'.format(params['protocol'],cluster)


    # PCE4 = pd.DataFrame(columns = ['P3'], index = taus*1e6)

    filename = 'done.csv'
    
        
    if path.exists(Dir + filename):
        done = pd.read_csv(Dir + filename,index_col = 0).values.tolist()
        
    else: done = []
    done = []
    

    if pbar == True:
    
        for s in tqdm(spins,desc = 'CCE2',position = 0):
            for m in spins:
                
                lst = [s,m];
                lst.sort()
                if (lst not in done) & (m != s) & (couplings['C{}'.format(m)].loc[s] >= 0.5):
                    
                    
                    operators = nv.generate_full_H0(operators,
                                               couplings.loc[[s,m]],
                                               params = params,
                                               CC_coupling = CC_coupling)
                    L2 = [];
                    for t in ts:
                        
                        params['tau'] = t
                        params['t_ev'] = t
                        
                        Ltemp, rho = nv.pulse_NV(operators,params,measure = measure)
                        L2.append(Ltemp.real)
                
                    

                    # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                    sub_sys = [s,m]
                    CCE2 = pd.DataFrame(L2,columns = ['coherence'],index = ts)
                    sub_sys.sort()

                    filename_CCE = 'C{}_C{}.csv'.format(sub_sys[0],sub_sys[1])
                    CCE2.to_csv(Dir + filename_CCE)
                
                    done.append(lst);
                        
    else:
    
        for s in spins:
            for m in spins:
                
                lst = [s,m];
                lst.sort()
                if (lst not in done) & (m != s) & (couplings['C{}'.format(m)].loc[s] >= 0.5):
                    
                    
                    operators = nv.generate_full_H0(operators,
                                               couplings.loc[[s,m]],
                                               params = params,
                                               CC_coupling = CC_coupling)
                    L2 = [];
                    for t in ts:
                        
                        params['tau'] = t
                        params['t_ev'] = t
                        
                        Ltemp, rho = nv.pulse_NV(operators,params,measure = measure)
                        L2.append(Ltemp.real)
                
                    
    
                    # PCE4['P4_%d_%d_%d'%(s,p,q)] = np.array(P4)
                    sub_sys = [s,m]
                    CCE2 = pd.DataFrame(L2,columns = ['coherence'],index = ts)
                    sub_sys.sort()
    
                    filename_CCE = 'C{}_C{}.csv'.format(sub_sys[0],sub_sys[1])
                    CCE2.to_csv(Dir + filename_CCE)
                
                    done.append(lst);

    done_df = pd.DataFrame(done)
    done_df.to_csv(Dir + filename)
    
    return done_df