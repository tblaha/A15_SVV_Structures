# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:56:53 2019

@author: Till
"""
import numpy as np
import matplotlib.pyplot as plt


def vonMises(sigmas, taus):
    
    return np.sqrt( ((sigmas[0] - sigmas[1])**2 + (sigmas[1] - sigmas[2])**2 + (sigmas[2] - sigmas[0])**2\
            + 6*(taus[0]**2 + taus[1]**2 + taus[2]**2)) / 2 )
    
    
def getVonMises(B, M_y_int, M_z_int, I_yy, I_zz, Shear_Final, q_B_intro, t_sk, t_sp):
    
    # normal stresses do to bending
    Dy = B[:,0]
    Dz = B[:,1]
    
    vonMises_atx = np.zeros(len(B))
    all_q_B_intro = np.zeros(len(B))
    all_q_B_intro[0:len(q_B_intro)] = q_B_intro
    
    total_q   = Shear_Final + all_q_B_intro
    total_tau = np.zeros(len(total_q))
    
    # not spar
    total_tau[np.where(B[:,4] != 3)] = total_q[np.where(B[:,4] != 3)]  / t_sk
    
    # spar
    total_tau[np.where(B[:,4] == 3)] = total_q[np.where(B[:,4] == 3)]  / t_sp
    
    i = 0
    for boom in range(len(B)):
        
        sigmas    = np.zeros(3)
        taus      = np.zeros(3)
        sigmas[0] = M_z_int * Dy[i] / I_zz - M_y_int * Dz[i] / I_yy
        taus[0]   = total_tau[i]
        
        vonMises_atx[i] = vonMises(sigmas, taus)
        i = i + 1
        
    return vonMises_atx
    

def plotVonMises(fig_id, B, vonMises_in_ribs, ribName):
    
    plt.ioff()
    
    plt.figure(fig_id, figsize=(7.5, 4.5))
    plt.clf()
    axs = plt.axes()
    
    plt.scatter(B[:,1], B[:,0], c=vonMises_in_ribs, cmap='jet')
    plt.title('Numerical Model -- von Mises Stress Rib ' + ribName + ' -- Maximum: %.2f MPa' % np.max(vonMises_in_ribs))
    axs.invert_xaxis()
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    cbar = plt.colorbar()
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    
    plt.savefig('Plots/Numerical_rib' + ribName + '_scatter.eps', format='eps')
    
    plt.ion()
    
    
x_loc_idx = 113
x_loc_idx_2 = 114

# get panel shears
Qb_z, Qb_y,B_Distance,Line_Integral_qb_3,A,b,shear_vec,Shear_Final=baseShearFlows(I_zz,I_yy,SFIz[x_loc_idx],SFIy[x_loc_idx],cross_disc,MIx[x_loc_idx],z_bar)
Qb_z, Qb_y,B_Distance,Line_Integral_qb_3,A,b,shear_vec,Shear_Final_2=baseShearFlows(I_zz,I_yy,SFIz[x_loc_idx_2],SFIy[x_loc_idx_2],cross_disc,MIx[x_loc_idx_2],z_bar)
#Rib B
#q_B,q_1_B,q_2_B=shearFlowRib(cross_disc, z_bar, y_bar, P_1=P_1, P_2=0, F_z=0*Fz[1]*0.5, F_y=0*Fy[1]*0.5)


vonMises_in_rib = getVonMises(cross_disc, 0*MIy[x_loc_idx], 0*MIz[x_loc_idx], 9.9e7, 1.2e7, Shear_Final[:,1]-Shear_Final_2[:,1], 0*q_B, t_sk, t_sp)
vonMises_in_rib_q_B = getVonMises(cross_disc, 0*MIy[x_loc_idx], 0*MIz[x_loc_idx], 9.9e7, 1.2e7, 0*Shear_Final[:,1], q_B, t_sk, t_sp)

plotVonMises(100, cross_disc, vonMises_in_rib, 'B')
plotVonMises(101, cross_disc, vonMises_in_rib_q_B, 'B_alt')



