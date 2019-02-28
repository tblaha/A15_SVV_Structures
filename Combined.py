# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:49:58 2019

@author: daanv
"""

import numpy as np
import matplotlib.pyplot as plt

from Centroid import findCentroid
from DiscretizationV2 import discretizeCrossSection, discretizeSpan
from DiscretizationMOI import discretizeCrossSectionMOI #Calculates booms for the MOI in the verification case
from InternalLoads import getInternalLoads
from MomentOfInertia import momentOfInertia
from ReactionForcesV2 import sampleBendingShape
from ShapeOfAileron import shapeOfAileron
from ShearFlowsFinal import baseShearFlows
from ShearFlowRibs import shearFlowRib
from Stiffeners import generateStiffeners
from UniversalConstants import \
h_a,c_a,n_st,A_st,t_sk,t_sp,Ybar_st,x_h1,x_h2,x_h3,l_a,d_a,p,q,theta,d_1,d_3,E,G 
from VerInternalLoads import getVerInternalLoads
from vonMises import *
from InterpretFEMData import *

#Verification
VerificationAssumptions=False #Adjusts the program so that the program matches the analytical model as closely as possible.

#Variables to be chosen:
span_nodes_between=20 #How many nodes between two points of interest
span_ec=0.001 #How close should the first point be to the point of interest
span_offset=30 #How concentrated should the points be (Lower is higher concentration)
booms_between=20 #The amount of booms between each centre
cg_cor_stiffeners=1 #Correct for the stiffeners centroid or not

#plots
plotBending=False #Plots the bending shape
plotSpan=False #Plots the distribution of the points in which forces are calculated
plotInternal=False #Plots the internal shear and moment diagrams
plotVerInternal=False #Plots Internal loads in a diagram with the analytical internal loads
plotAileron=False #Plots a simplified version of the aileron.
plotDeflectionsTheta0=False	#Plots the displacements of the LE and TE compared to where they would be if theta was 0 and there was no loading.
plotDeflections=False #Plots the displacements of the LE and TE compared to where they would be if there was no loading.


#prints
printInfo=False #Prints all chosen variables
printInputs=False #Prints actual input values for booms_between,span_nodes_between
printOutputs=False #Prints the actual output of the program
printReactionForces=False #Prints all reaction forces 
printMOI=False #Prints Moment of Inertia 


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
if plotSpan==False:
    plt.plot(span_disc,len(span_disc)*[1],'x')
    plt.show()


#Check which discretization to use and discretize the cross section
if VerificationAssumptions:
    cross_disc=discretizeCrossSectionMOI(S_cor,S_uncor,h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, cg_cor_stiffeners)
    z_bar=0 #done after the calculations for MOI to not upset the boom discretization
else:
    cross_disc=discretizeCrossSection(S_cor,S_uncor,h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, cg_cor_stiffeners)

##Calc MOI
I_zz,I_yy = momentOfInertia(cross_disc)
    
## Get bending and reaction forces
d_yz_vec, F_2x, Fy, Fz, P_1 = sampleBendingShape(span_disc, x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3,  E,  I_yy, I_zz, 1, 2700e0, 27e3)


#Plot bending shape if enabled
if plotBending==False:
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(span_disc, d_yz_vec[0,:])
    axs[1].plot(span_disc, d_yz_vec[1,:])
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
##Get Internal Loads

SFIx, SFIy, SFIz, MIx, MIy, MIz = getInternalLoads(span_disc,F_2x, Fy, Fz, P_1)

#Plot internal loads if enabled, 6 plots
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

#Generates 6 plots, each containing both the Analytical model's values and the 
#Numerical model's values
if plotVerInternal:
    if theta==26:
        case=1
    elif theta==0:
        case=0
    else:
        case=2
    #NOTE: Order is not the same as that within VerInternalLoads.py
    #this is due to an error in the analytical model, do not fix
    xVer,VzVer,VyVer,MyVer,MzVer,MxVer=getVerInternalLoads(case)
    titleFontSize=14
    axisFontSize=12
    plt.subplot(231)
    plt.plot(span_disc,SFIx,'b')
    plt.plot(xVer,xVer*[0],'r')
    plt.xlabel('x-position [mm]', fontsize=axisFontSize)
    plt.ylabel('Internal force [N]', fontsize=axisFontSize)
    plt.title('Internal normal force x', fontsize=titleFontSize)
    
    plt.subplot(232)
    plt.plot(span_disc,SFIy,'b')
    plt.plot(xVer,VyVer,'r')
    plt.xlabel('x-position [mm]', fontsize=axisFontSize)
    plt.ylabel('Internal shear force [N]', fontsize=axisFontSize)
    plt.title('Internal shear force y', fontsize=titleFontSize)
    
    plt.subplot(233)
    plt.plot(span_disc,SFIz,'b')
    plt.plot(xVer,VzVer,'r')
    plt.xlabel('x-position [mm]', fontsize=axisFontSize)
    plt.ylabel('Internal shear force [N]', fontsize=axisFontSize)
    plt.title('Internal shear force z', fontsize=titleFontSize)
    
    plt.subplot(234)
    plt.plot(span_disc,MIx,'b')
    plt.plot(xVer,MxVer,'r')
    plt.xlabel('x-position [mm]', fontsize=axisFontSize)
    plt.ylabel('Moment [N/mm]', fontsize=axisFontSize)
    plt.title('Internal moment x', fontsize=titleFontSize)
    
    plt.subplot(235)
    plt.plot(span_disc,MIy,'b',label='Numerical model result')
    plt.plot(xVer,MyVer,'r',label='Analytical model result')
    plt.xlabel('x-position [mm]', fontsize=axisFontSize)
    plt.ylabel('Moment [N/mm]', fontsize=axisFontSize)
    plt.title('Internal moment y', fontsize=titleFontSize)
    plt.legend(loc=8)
    
    plt.subplot(236)
    plt.plot(span_disc,MIz,'b')
    plt.plot(xVer,MzVer,'r')
    plt.xlabel('x-position [mm]', fontsize=axisFontSize)
    plt.ylabel('Moment [N/mm]', fontsize=axisFontSize)
    plt.title('Internal moment z', fontsize=titleFontSize)
    
    plt.show ()

##Compute dtheta dx
dtdx=np.zeros(len(span_disc))
for i in range(len(span_disc)):
    x=span_disc[i]
    Qb_z, Qb_y,B_Distance,Line_Integral_qb_3,A,b,shear_vec,Shear_Final=baseShearFlows(I_zz,I_yy,SFIz[i],SFIy[i],cross_disc,MIx[i],z_bar)
    dtdx[i]=shear_vec[2]/(G)



##Interpret the FEM (saves plots without showing them)
FEMversion = ''
#FEMversion = ''
arc_coords, S_post_ribs, U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE = InterpretFEM(h_a, c_a, FEMversion)

##Compute shape of aileron    
disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x, displ_le, displ_te, section_thetas=shapeOfAileron(span_disc, d_yz_vec, dtdx, z_bar, plot_aileron=plotAileron, plot_deflections_theta_0=plotDeflectionsTheta0, plot_deflections=plotDeflections)
plotLETE(U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE, FEMversion, span_disc, displ_le, displ_te)

FEMversion = '_V2'
#FEMversion = ''
arc_coords, S_post_ribs, U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE = InterpretFEM(h_a, c_a, FEMversion)

##Compute shape of aileron    
disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x, displ_le, displ_te, section_thetas=shapeOfAileron(span_disc, d_yz_vec, dtdx, z_bar, plot_aileron=plotAileron, plot_deflections_theta_0=plotDeflectionsTheta0, plot_deflections=plotDeflections)
plotLETE(U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE, FEMversion, span_disc, displ_le, displ_te)


####Compute the shear flow in the ribs
systemOfEquationsForShearRib = shearFlowRib(cross_disc, z_bar, y_bar)
#Rib A, Fy1,Fz1
q_A,q_1_A,q_2_A=systemOfEquationsForShearRib.calculateShear(P_1=0, P_2=0, F_z=Fz[0], F_y=Fy[0])
#Rib B
q_B,q_1_B,q_2_B=systemOfEquationsForShearRib.calculateShear(P_1=P_1, P_2=0, F_z=Fz[1]*0.5, F_y=Fy[1]*0.5)
#Rib C
q_C,q_1_C,q_2_C=systemOfEquationsForShearRib.calculateShear(P_1=0, P_2=p, F_z=Fz[1]*0.5, F_y=Fy[1]*0.5)
#Rib D
q_D,q_1_D,q_2_D=systemOfEquationsForShearRib.calculateShear(P_1=0, P_2=0, F_z=Fz[2], F_y=Fy[2])




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
    print('cg_cor_stiffeners=',cg_cor_stiffeners)
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