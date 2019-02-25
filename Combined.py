# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:49:58 2019

@author: daanv
"""

import numpy as np
import matplotlib.pyplot as plt

from Centroid import *
from discretization import *
from InternalLoads import *
from MomentOfInertia import *
from ReactionForcesV2 import *
from ShapeOfAileron import *
from ShearFlows import *
from Stiffeners import *
from UniversalConstants import *

#Variables to be chosen:
span_nodes_between=50 #How many nodes between two points of interest
span_ec=0.0001 #How close should the first point be to the point of interest
span_offset=30 #How concentrated should the points be (Lower is higher concentration)
booms_between=0 #The amount of booms between each centre

#Extra outputs
plotBending=False #Plots the bending shape
plotSpan=False #Plots the distribution of the points in which forces are calculated
plotInternal=False #Plots the internal shear and moment diagrams
plotDisplacements=False #Plot the displacements of the aileron
printInfo=False #Prints all chosen variables
printInputs=False #Prints actual input values for booms_between,span_nodes_between

#Generate stiffener locations
Stiffeners = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp)

#Finding the centroid (small letter due to reference system)
y_bar,z_bar=findCentroid(Stiffeners)

##Discretize spanwise
span_disc=discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, span_nodes_between,span_ec,span_offset)

#Plot spanwise distribution of nodes if enabled
if plotSpan==True:
    plt.plot(span_disc,len(span_disc)*[1],'x')
    plt.show()

##Discretize cross-section
cross_disc=discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between)

##Calc MOI
I_zz,I_yy = MomentOfInertia(cross_disc)

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
if plotInternal==True:
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

##Compute dtheta dz
dtdz=np.zeros(len(span_disc))
for i in range(len(span_disc)):
    x=span_disc[i]
    Qb_z, Qb_y,B_Distance,Line_Integral_qb,Line_Integral_qb_1,Line_Integral_qb_2,Line_Integral_qb_3,A,b,shear_vec=baseShearFlows(I_zz,I_yy,SFIz[i],SFIy[i],cross_disc,MIx[i],z_bar)
    dtdz_x=shear_vec[2]
    dtdz[i]=dtdz_x

##Compute shape of aileron    
disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x=shapeOfAileron(span_disc, d_yz_vec, dtdz, theta, z_bar, plot=plotDisplacements)


#Print info if enabled
if printInfo==True:
    print('The following run had a total of', len(span_disc),\
          'spanwise nodes, with a distance of', span_ec,\
          '[mm] with a distribution coefficient of', span_offset)
    print('For the boom discretization a total of', len(cross_disc), 'booms were used')

#Print inputs if enabled
if printInputs==True:
    print('span_nodes_between=',span_nodes_between)
    print('span_ec=',span_ec)
    print('span_offset=',span_offset)
    print('booms_between=',booms_between)
    
#Print output
print('Maximum displacement in Y of the leading edge: ', disp_le_y_max, '[mm] at X coordinate: ', disp_le_max_x, '[mm]')
print('Maximum displacement in Y of the trailing edge: ', disp_te_y_max, '[mm] at X coordinate: ', disp_te_max_x, '[mm]')
