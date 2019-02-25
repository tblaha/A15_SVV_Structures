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
#from ShapeOfAileron import *
#from ShearFlows import *
from Stiffeners import *
from UniversalConstants import *

Izzactual=1.252E+07
Iyyactual=9.934E+07


Izzlist=[]
Iyylist=[]
for i in range(50):
    
    booms_between=i #The amount of booms between each centre
    
    #Generate stiffener locations
    Stiffeners = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 1)
    
    #Finding the centroid (small letter due to reference system)
    y_bar,z_bar=findCentroid(Stiffeners)
    
    ##Discretize cross-section
    cross_disc=discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, Ybar_st, booms_between, 1)
    
    ##Calc MOI
    I_zz,I_yy = MomentOfInertia(cross_disc)
    Izzlist.append(I_zz)
    Iyylist.append(I_yy)
    
plt.subplot(121)
plt.plot(range(50),Izzlist)
plt.plot(range(50),Izzactual*np.ones((50,1)))
plt.subplot(122)
plt.plot(range(50),Iyylist)
plt.plot(range(50),Iyyactual*np.ones((50,1)))
plt.show()