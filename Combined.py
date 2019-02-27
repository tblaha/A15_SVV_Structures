# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:49:58 2019

@author: daanv
"""

import numpy as np
import matplotlib.pyplot as plt

from Centroid import findCentroid
from DiscretizationV2 import discretizeCrossSection, discretizeSpan
from DiscretizationMOI import discretizeCrossSectionMOI #Calculates booms for the verification case
from InternalLoads import getInternalLoads
from MomentOfInertia import momentOfInertia
from ReactionForcesV2 import sampleBendingShape
from ShapeOfAileron import shapeOfAileron
from ShearFlowsFinal import baseShearFlows
from ShearFlowRibs import shearFlowRib
from Stiffeners import generateStiffeners
from UniversalConstants import *
from vonMises import *
from InterpretFEMData import *

#Verification
VerificationAssumptions=False #Adjusts the program so that the program matches the analytical model as closely as possible.

#Variables to be chosen:
span_nodes_between=20 #How many nodes between two points of interest
span_ec=0.001 #How close should the first point be to the point of interest
span_offset=30 #How concentrated should the points be (Lower is higher concentration)
booms_between=200 #The amount of booms between each centre
cg_cor_stiffeners=1 #Correct for the stiffeners centroid or not

#Extra outputs
plotBending=False #Plots the bending shape
plotSpan=False #Plots the distribution of the points in which forces are calculated
plotInternal=False #Plots the internal shear and moment diagrams
plotAileron=True #Plots a simplified version of the aileron.
plotDeflectionsTheta0=True	#Plots the displacements of the LE and TE compared to where they would be if theta was 0 and there was no loading.
plotDeflections=True #Plots the displacements of the LE and TE compared to where they would be if there was no loading.
printInfo=False #Prints all chosen variables
printInputs=False #Prints actual input values for booms_between,span_nodes_between
printOutputs=True #Prints the actual output of the program
printReactionForces=False #Prints all reaction forces 
printMOI=True #Prints Moment of Inertia 
 

#Generate stiffener locations
S_uncor = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 0)
S_cor = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 1)
if cg_cor_stiffeners==1:
    Stiffeners=S_cor
else:
    Stiffeners=S_uncor


#Finding the centroid (small letter due to reference system)
y_bar,z_bar=findCentroid(Stiffeners)

##Discretize spanwise
span_disc=discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, span_nodes_between,span_ec,span_offset)

#Plot spanwise distribution of nodes if enabled
if plotSpan==True:
    plt.plot(span_disc,len(span_disc)*[1],'x')
    plt.show()


#Check which discretization to use and discretize the cross section
if VerificationAssumptions:
    cross_disc=discretizeCrossSectionMOI(S_cor,S_uncor,h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, cg_cor_stiffeners)
    z_bar=0 #done after the calculations for MOI to not upset the boom discretization
else:
    cross_disc=   discretizeCrossSection(S_cor,S_uncor,h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, cg_cor_stiffeners)

##Calc MOI
I_zz,I_yy = momentOfInertia(cross_disc)
    
## Get bending and reaction forces
## don't worry about the magic numbers at the end. I tried including Timoshenko shear deformations, but it doesnt make much of a difference
d_yz_vec, F_2x, Fy, Fz, P_1 = sampleBendingShape(span_disc, x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3,  E,  I_yy, I_zz, 1, 1200e10, 27e3)


#Plot bending shape if enabled
if plotBending==True:
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(span_disc, d_yz_vec[0,:])
    axs[1].plot(span_disc, d_yz_vec[1,:])
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
##Get Internal Loads

SFIx, SFIy, SFIz, MIx, MIy, MIz = getInternalLoads(span_disc,F_2x, Fy, Fz, P_1)

#Plot internal loads if enabled
if plotInternal:
    plt.subplot(231)
    plt.plot(span_disc,SFIx)
    plt.title('Internal normal force x')
    
    plt.subplot(232)
    plt.plot(span_disc,SFIy)
    plt.title('Internal shear force y')
    
    plt.subplot(233)
    plt.plot(span_disc,SFIz)
    plt.title('Internal shear force z')
    
    plt.subplot(234)
    plt.plot(span_disc,MIx)
    plt.title('Internal moment x')
    
    plt.subplot(235)
    plt.plot(span_disc,MIz)
    plt.title('Internal moment z')
    
    plt.subplot(236)
    plt.plot(span_disc,MIy)
    plt.title('Internal moment y')
    
    plt.show ()

##Compute dtheta dx
dtdx=np.zeros(len(span_disc))
for i in range(len(span_disc)):
    x=span_disc[i]
    Qb_z, Qb_y,B_Distance,Line_Integral_qb_3,A,b,shear_vec,Shear_Final=baseShearFlows(I_zz,I_yy,SFIz[i],SFIy[i],cross_disc,MIx[i],z_bar)
    dtdx[i]=shear_vec[2]/(G)



##Interpret the FEM (saves plots without showing them)
arc_coordinates, vonMises_ribs = InterpretFEM(h_a, c_a)


##Compute shape of aileron    
disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x=shapeOfAileron(span_disc, d_yz_vec, dtdx, z_bar, plot_aileron=plotAileron, plot_deflections_theta_0=plotDeflectionsTheta0, plot_deflections=plotDeflections)

## WARNING; TAKE THIS OUT LATER, bullshit FEM values
Fz[0] = -3.93*1e3
Fz[2] =  5.35*1e3
Fy[0] = 22.9*1e3
Fy[2] = 19.4*1e3

##Compute the shear flow in the ribs
#Rib A, Fy1,Fz1
q_A,q_1_A,q_2_A=shearFlowRib(cross_disc, z_bar, y_bar, P_1=0, P_2=0, F_z=Fz[0], F_y=Fy[0])
#Rib B
q_B,q_1_B,q_2_B=shearFlowRib(cross_disc, z_bar, y_bar, P_1=P_1, P_2=0, F_z=0*Fz[1]*0.5, F_y=0*Fy[1]*0.5)
#Rib C
q_C,q_1_C,q_2_C=shearFlowRib(cross_disc, z_bar, y_bar, P_1=0, P_2=p, F_z=0*Fz[1]*0.5, F_y=0*Fy[1]*0.5)
#Rib D
q_D,q_1_D,q_2_D=shearFlowRib(cross_disc, z_bar, y_bar, P_1=0, P_2=0, F_z=Fz[2], F_y=Fy[2])



# von Mises in ribs (skin stress just before, then add the rib shear)
vonMises_A, Qb_y_A, Qb_z_A = getVonMises(x_h1      , span_disc, cross_disc, SFIz, SFIy, MIx, MIy, MIz, I_yy, I_zz, t_sk, t_sp, z_bar, q_A)
plotVonMises(cross_disc, vonMises_A, 'von Mises Stress at Rib A', 'S_at_A_vM')
vonMises_B, Qb_y_B, Qb_z_B = getVonMises(x_h2-d_a/2, span_disc, cross_disc, SFIz, SFIy, MIx, MIy, MIz, I_yy, I_zz, t_sk, t_sp, z_bar, q_B)
plotVonMises(cross_disc, vonMises_B, 'von Mises Stress at Rib B', 'S_at_B_vM')
vonMises_C, Qb_y_C, Qb_z_C = getVonMises(x_h2+d_a/2, span_disc, cross_disc, SFIz, SFIy, MIx, MIy, MIz, I_yy, I_zz, t_sk, t_sp, z_bar, q_C)
plotVonMises(cross_disc, vonMises_C, 'von Mises Stress at Rib C', 'S_at_C_vM')
vonMises_D, Qb_y_D, Qb_z_D = getVonMises(x_h3      , span_disc, cross_disc, SFIz, SFIy, MIx, MIy, MIz, I_yy, I_zz, t_sk, t_sp, z_bar, q_D)
plotVonMises(cross_disc, vonMises_D, 'von Mises Stress at Rib D', 'S_at_D_vM')



#before Rib

# von Mises at other locations (w/out ribs)
vM_locs = [0,l_a/2,l_a, 600, 700, 200, 800]
vonMises_others = np.zeros((len(vM_locs), len(cross_disc)))
Qb_y_others = np.zeros((len(vM_locs), len(cross_disc)))
Qb_z_others = np.zeros((len(vM_locs), len(cross_disc)))

for idx in range(len(vM_locs)):
    vonMises_others[idx], Qb_y_others[idx], Qb_z_others[idx] = getVonMises(vM_locs[idx], span_disc, cross_disc, SFIz, SFIy, MIx, MIy, MIz, I_yy, I_zz, t_sk, t_sp, z_bar, q_A)
    plotVonMises(cross_disc, vonMises_others[idx], 'von Mises Skin Stress at x=%d' % vM_locs[idx], 'S_at_x_%d_vM'   % vM_locs[idx])
    plotVonMises(cross_disc, Qb_y_others[idx]    , 'Qb_y at x=%d' % vM_locs[idx]                 , 'S_at_x_%d_qb_y' % vM_locs[idx])
    plotVonMises(cross_disc, Qb_z_others[idx]    , 'Qb_z at x=%d' % vM_locs[idx]                 , 'S_at_x_%d_qb_z' % vM_locs[idx])










#
#
#
#
###Compute von Mises stresses around the Ribs
#ribA_idx = sum((span_disc - x_h1-80)         < 0)-1
#ribB_idx = sum((span_disc - (x_h2-d_a/2)) < 0)-1
#ribC_idx = sum((span_disc - (x_h2+d_a/2)) < 0)-1
#ribD_idx = sum((span_disc - x_h3)         < 0)-1
#
#dum1,dum2,dum3,dum4,dum5,dum6,dum7,Shear_Final_A = baseShearFlows(I_zz,I_yy,SFIz[ribA_idx],SFIy[ribA_idx],cross_disc,MIx[ribA_idx],z_bar)
#dum1,dum2,dum3,dum4,dum5,dum6,dum7,Shear_Final_B = baseShearFlows(I_zz,I_yy,SFIz[ribB_idx],SFIy[ribB_idx],cross_disc,MIx[ribB_idx],z_bar)
#dum1,dum2,dum3,dum4,dum5,dum6,dum7,Shear_Final_C = baseShearFlows(I_zz,I_yy,SFIz[ribC_idx],SFIy[ribC_idx],cross_disc,MIx[ribC_idx],z_bar)
#dum1,dum2,dum3,dum4,dum5,dum6,dum7,Shear_Final_D = baseShearFlows(I_zz,I_yy,SFIz[ribD_idx],SFIy[ribD_idx],cross_disc,MIx[ribD_idx],z_bar)
#
#vonMises_ribA = getVonMises(cross_disc, MIy[ribA_idx], MIz[ribA_idx], I_yy, I_zz, 0*Shear_Final_A[:,1], 0*q_A, t_sk, t_sp)
#vonMises_ribB = getVonMises(cross_disc, 0*MIy[ribB_idx], 0*MIz[ribB_idx], I_yy, I_zz, Shear_Final_B[:,1], 0*q_B, t_sk, t_sp)
#vonMises_ribC = getVonMises(cross_disc, 0*MIy[ribC_idx], 0*MIz[ribC_idx], I_yy, I_zz, Shear_Final_C[:,1], 0*q_C, t_sk, t_sp)
#vonMises_ribD = getVonMises(cross_disc, 0*MIy[ribD_idx], 0*MIz[ribD_idx], I_yy, I_zz, Shear_Final_D[:,1], 0*q_D, t_sk, t_sp)
#
#plotVonMises(100, cross_disc, vonMises_ribA, 'A') # only saves plots, doesn't show
#plotVonMises(101, cross_disc, vonMises_ribB, 'B')
#plotVonMises(102, cross_disc, vonMises_ribC, 'C')
#plotVonMises(103, cross_disc, vonMises_ribD, 'D')
#
#Qbz,Qby,dum3,dum4,dum5,dum6,dum7,Shear_Final_A = baseShearFlows(I_zz,I_yy,SFIz[ribB_idx],SFIy[ribB_idx],cross_disc,MIx[ribB_idx],z_bar)
#vonMises_ribB_Qbz = getVonMises(cross_disc, 0*MIy[ribA_idx], 0*MIz[ribA_idx], I_yy, I_zz, Qbz[:,1], 0*q_A, t_sk, t_sp)
#vonMises_ribB_Qby = getVonMises(cross_disc, 0*MIy[ribA_idx], 0*MIz[ribA_idx], I_yy, I_zz, Qby[:,1], 0*q_A, t_sk, t_sp)
#plotVonMises(104, cross_disc, vonMises_ribB_Qbz, 'B_Qbz') # only saves plots, doesn't show
#plotVonMises(105, cross_disc, vonMises_ribB_Qby, 'B_Qby')


# basic FEM post processing
InterpretFEM(h_a, c_a)



#Print info if enabled
if printInfo:
    print('The following run had a total of', len(span_disc),\
          'spanwise nodes, with a distance of', span_ec,\
          '[mm] with a distribution coefficient of', span_offset)
    print('For the boom discretization a total of', len(cross_disc), 'booms were used')

#Print inputs if enabled
if printInputs:
    print('span_nodes_between=',span_nodes_between)
    print('span_ec=',span_ec)
    print('span_offset=',span_offset)
    print('booms_between=',booms_between)
    
#Print output
if printOutputs:
    print('Maximum displacement in Y of the leading edge: ', disp_le_y_max, '[mm] at X coordinate: ', disp_le_max_x, '[mm]')
    print('Maximum displacement in Y of the trailing edge: ', disp_te_y_max, '[mm] at X coordinate: ', disp_te_max_x, '[mm]')
    print('Magnitude of the maximum shear flow in rib A: ', max(abs(q_A)), '[N/mm]')
    print('Magnitude of the maximum shear flow in rib B: ', max(abs(q_B)), '[N/mm]')
    print('Magnitude of the maximum shear flow in rib C: ', max(abs(q_C)), '[N/mm]')
    print('Magnitude of the maximum shear flow in rib D: ', max(abs(q_D)), '[N/mm]')
    
if printReactionForces==True: #Prints all reaction forces 
    print('Fyh1,2,3,Fzh1,2,3,P_1',Fy,Fz,P_1) 
     
if printMOI==True: #Prints Moment of Inertia 
    print('Iyy=', I_yy) 
    print('Izz=', I_zz) 
     