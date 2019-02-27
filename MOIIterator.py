# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:49:58 2019

@author: daanv
"""

import numpy as np
import matplotlib.pyplot as plt

from Centroid import *
from DiscretizationMOI import *
from InternalLoads import *
from MomentOfInertia import *
from ReactionForcesV2 import *
#from ShapeOfAileron import *
#from ShearFlows import *
from Stiffeners import *
from UniversalConstants import *

Izzactual=1.252E+07
Iyyactual=9.934E+07

##50 Booms
#Iyy= 97028265.30805449
#Izz= 12556285.832960596
##100 Booms
#Iyy= 97176018.87363233
#Izz= 12545621.129745593
##150 Booms
#Iyy= 97226010.9787685
#Izz= 12542104.797035603
#
#print(Izzactual/Izz)
#print(Iyyactual/Iyy)

Izzlist=[]
Iyylist=[]
max_booms = 200

for i in range(max_booms):
    
    booms_between=i #The amount of booms between each centre
    
    #Generate stiffener locations
    Stiffeners = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 0)
    Stiffeners_corrected = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 1)
    
    #Finding the centroid (small letter due to reference system)
    y_bar,z_bar=findCentroid(Stiffeners_corrected)
    
    ##Discretize cross-section
    cross_disc=discretizeCrossSection(Stiffeners, Stiffeners_corrected, h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, 0)
    
    ##Calc MOI
    I_zz,I_yy = MomentOfInertia(cross_disc)
    Izzlist.append(I_zz)
    Iyylist.append(I_yy)
    
plt.subplot(121)
plt.plot(range(max_booms),Izzlist)
plt.plot(range(max_booms),Izzactual*np.ones((max_booms,1)))
plt.subplot(122)
plt.plot(range(max_booms),Iyylist)
plt.plot(range(max_booms),Iyyactual*np.ones((max_booms,1)))
plt.show()


# plot discretizations
#B    = discretizeCrossSection(Stiffeners, Stiffeners_corrected, h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, 0)
#Balt = discretizeCrossSection(Stiffeners, Stiffeners_corrected, h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, booms_between, Ybar_st, 1)

#plotCrossSection(B, Balt)