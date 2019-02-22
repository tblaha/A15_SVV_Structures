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
from ReactionForces import *
#from ShapeOfAileron import *
#from ShearFlows import *
from Stiffeners import *
from UniversalConstants import *

#Variables to be chosen:
span_nodes_between=50 #How many nodes between two points of interest
span_ec=0.0001 #How close should the first point be to the point of interest
span_offset=30 #How concentrated should the points be (Lower is higher concentration)
booms_between=20 #The amount of booms between each centre
plotBending=0
plotInternal=1

#Generate stiffener locations
Stiffeners = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp)

#Finding the centroid (small letter due to reference system)
y_bar,z_bar=findCentroid(Stiffeners)

##Discretize spanwise
span_disc=discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, span_nodes_between,span_ec,span_offset)

##Discretize cross-section
cross_disc=discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between)

##Calc MOI
I_zz,I_yy = MomentOfInertia(cross_disc)

##Get bending and reaction forces
d_yz_vec, Fx, Fy, Fz, P_1 = sampleBendingShape(span_disc, x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_zz, I_yy)

if plotBending==1:
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(span_disc, d_yz_vec[0,:])
    axs[1].plot(span_disc, d_yz_vec[1,:])
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
##Get Internal Loads

SFIx, SFIy, SFIz, MIx, MIy, MIz = getInternalLoads(span_disc,Fx, Fy, Fz, P_1)

if plotInternal==1:
    plt.subplot(231)
    plt.plot(span_disc,SFIx)
    plt.title('Internal shear force x')
    
    plt.subplot(232)
    plt.plot(span_disc,SFIy)
    plt.title('Internal shear foce y')
    
    plt.subplot(233)
    plt.plot(span_disc,SFIz)
    plt.title('Internal shear force z')
    
    plt.subplot(234)
    plt.plot(span_disc,MIx)
    plt.title('Internal moment x')
    
    plt.subplot(235)
    plt.plot(span_disc,MIy)
    plt.title('Internal moment y')
    
    plt.subplot(236)
    plt.plot(span_disc,MIz)
    plt.title('Internal moment z')
    plt.show ()
##Compute 




##    

