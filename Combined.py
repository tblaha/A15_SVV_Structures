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
d_yz_vec, Fx, Fy, Fz, P = sampleBendingShape(span_disc, x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_zz, I_yy)
PlotBending=0
if PlotBending==1:
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(span_disc, d_yz_vec[0,:])
    axs[1].plot(span_disc, d_yz_vec[1,:])
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
##Get Internal Loads
F_y_1 = Fy[0]
F_y_2 = Fy[1]
F_y_3 = Fy[2]

F_z_1 = Fy[0]
F_z_2 = Fy[1]
F_z_3 = Fy[2]

InternalShearForcey(Span_disc)

##Compute 




##    

