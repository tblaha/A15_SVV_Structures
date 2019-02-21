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
from ShapeOfAileron import *
from ShearFlows import *
from Stiffeners import *
from UniversalConstants import *

#Variables to be chosen:
span_nodes_between=50 #How many nodes between two points of interest
span_ec=0.0001 #How close should the first point be to the point of interest
span_offset=30 #How concentrated should the points be (Lower is higher concentration)
booms_between=20 #The amount of booms between each centre



#Generate stiffener locations
Stiffeners = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp)
print(Stiffeners)
#Finding the centroid (small letter due to reference system)
y_bar,z_bar=findCentroid(Stiffeners)

##Discretize spanwise
span_discretization=discretizeSpan(span_nodes_between,span_ec,span_offset)
#
##Discretize cross-section
cross_discretization=discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, cross=booms_between)

