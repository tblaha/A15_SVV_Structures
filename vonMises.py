# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:56:53 2019

@author: Till
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt
from ShearFlowsFinal import baseShearFlows


def vonMises(sigmas, taus):
    
    return np.sqrt( ((sigmas[0] - sigmas[1])**2 + (sigmas[1] - sigmas[2])**2 + (sigmas[2] - sigmas[0])**2\
            + 6*(taus[0]**2 + taus[1]**2 + taus[2]**2)) / 2 )



def getVonMises(xloc, span_disc, cross_disc, SFIz, SFIy, MIx, MIy, MIz, I_yy, I_zz, t_sk, t_sp, z_bar, q_B = []):
    
    # always select the location just to left or coincident with the x location
    x_idx = np.sum( span_disc - xloc <= 0)-1
    x_loc = span_disc[x_idx]
    
    vonMises_atx      = np.zeros(len(cross_disc))
    vonMises_atx_Qb_y = np.zeros(len(cross_disc))
    vonMises_atx_Qb_z = np.zeros(len(cross_disc))
    
    
    # process rib shear input (this awkward way of doing it was when Tuur
    # didn't have the spar ready yet)
    all_q_B             = np.zeros(len(cross_disc))
    all_q_B[0:np.min(np.array([len(cross_disc), len(q_B)]))] = q_B[0:np.min(np.array([len(cross_disc), len(q_B)]))]
    
    #(xloc, h_a, c_a, filename, all_nodes, rib_nodes=[])
    
    # call shear flow function
    Qb_z, Qb_y, B_Distance,Line_Integral_qb_3,A,b,shear_vec,Shear_Final=baseShearFlows(I_zz,I_yy,SFIz[x_idx],SFIy[x_idx],cross_disc,-MIx[x_idx],z_bar)
 
    
    # add the shear components
    total_q   = Shear_Final[:,1] + all_q_B   
    
    
    # shear stresses
    total_tau    = np.zeros(len(cross_disc))
    
    # not spar
    total_tau[np.where(cross_disc[:,4] != 3)] = total_q[np.where(cross_disc[:,4] != 3)]  / t_sk
    
    # spar
    total_tau[np.where(cross_disc[:,4] == 3)] = total_q[np.where(cross_disc[:,4] == 3)]  / t_sp
    
    
    
    # normal stresses do to bending
    Dy = cross_disc[:,0]
    Dz = cross_disc[:,1]-107
    
    i = 0
    for boom in range(len(cross_disc)):
        
        sigmas    = np.zeros(3)
        taus      = np.zeros(3)
        sigmas[0] = -MIz[x_idx] * Dy[i] / I_zz + MIy[x_idx] * Dz[i] / I_yy
        taus[0]   = total_tau[i]
        
        vonMises_atx[i]      = vonMises(sigmas, taus)
        
        i = i + 1
        
        
        
    return vonMises_atx, Qb_y[:,1], Qb_z[:,1]
    


def plotVonMises(B, vonMises_in_ribs, title, filename):
    
    plt.ioff()
    
    plt.figure(200, figsize=(7.5, 4.5))
    plt.clf()
    axs = plt.axes()
    
    plt.scatter(B[:,1], -B[:,0], c=vonMises_in_ribs, cmap='jet')
    plt.title('Numerical Model -- ' + title + ' -- Maximum: %.2f MPa' % np.max(vonMises_in_ribs))
    axs.invert_xaxis()
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    cbar = plt.colorbar()
    plt.clim(-100, 100)
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    
    plt.savefig('Plots/StressSections/' + filename + '.eps', format='eps')
    
    plt.ion()
    
    
def plotVonMisesBoth(B, FEMstresses, NUMstresses, xloc, nodes):
    
    plt.ioff()
    
    plt.figure(200, figsize=(10, 4))
    
    plt.clf()
    fig, axs = plt.subplots(1,2, figsize=(10, 4))#, sharex = True, sharey = True)
    plt.suptitle('Val. and Num. Model -- x = %d -- Maximum (Val.): %.2f MPa -- Maximum (Num.): %.2f MPa' % (xloc, np.max(FEMstresses), np.max(NUMstresses)))
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    axs[0].axis('equal')
    axs[1].axis('equal')
    
    # limit of colorbar (to the next 100MPa)
    if max(np.max(FEMstresses), np.max(NUMstresses)) >= 100:
        maxcolor = round(50+(max(np.max(FEMstresses), np.max(NUMstresses), -2)) )
    else:
        maxcolor = round(5+(max(np.max(FEMstresses), np.max(NUMstresses), -1)) )
    
    # Numerical
    axs[0].set_ylabel('y location [mm]', fontsize=14)
    axs[0].set_xlabel('z location [mm]', fontsize=14)
    axs[1].set_xlabel('z location [mm]', fontsize=14)
    
    im1=axs[0].scatter(nodes[:,3], nodes[:,2], c=FEMstresses, cmap='jet', vmin=0, vmax=maxcolor)
    im2=axs[1].scatter(B[:,1]-107, -B[:,0], c=NUMstresses, cmap='jet', vmin=0, vmax=maxcolor)
    cbar2 = fig.colorbar(im2)
    im2.set_clim(0,maxcolor)
    

    plt.tight_layout
    plt.savefig('Plots/CombinedStressSections/S_LC1_x_%d.eps' % xloc, format='eps')
    
    plt.ion()
    