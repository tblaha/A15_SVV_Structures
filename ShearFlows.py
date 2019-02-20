# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:57:40 2019

@author: patri
"""

import numpy as np
from UniversalConstants import *
from discretization import *

def baseShearFlows(I_zz,I_yy,V_z,V_y,B_array):
    #This function takes in the MOI parmeters as well as internal shear forces and 
    #cross sectional boom discretization.
    #The output is a 2D array with all the base shear flows in each segment
    #
    #---INPUTS---#
    #I_zz                : MOI about z axis
    #I_yy                : MOI about y axis
    #V_z                 : Internal shear foce in z direction
    #V_y                 : Internal shear force in y direction
    #B_Array:
    #2D array from disretization function which looks like:
     # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # cell id: 1 (exclusively left cell, anticlockwise sorted)
    #          2 (exclusively right cell, clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    #
    #---OUTPUTS---#
    #The output will be a 2D numpy array (Qb) with the numbered shear flows:
    #| q_i number | value |
    
    #Note q1 will be the represent the shear flow between boom 0 and 1 and so on
    
    #Create output arrays which will have the same number of rows as input boom area array
    Qb_z = np.zeros((len(B_array[:,0]),3))
    Qb_y = np.zeros((len(B_array[:,0]),3))
    
    #Initialize first cell
    ID=1
    
    #Looping across all the booms
    i=0
    
    #Do this for all 3 cells based on their IDs
    while ID<=3:
        
        #Initialize base shear at 0 in each cell as this will start from the
        #point of the cut
        qb_z=0
        qb_y=0
    
        
        #Do this until new cell/spar

        
        while ID!=ID+1:
            if i==128:
                break
            #Update Qb_z
            Qb_z[i,0]=i+1
            Qb_z[i,1]=qb_z
            Qb_z[i,2]=ID
            
            #Update Qb_y
            Qb_y[i,0]=i+1
            Qb_y[i,1]=qb_y
            Qb_y[i,2]=ID
            
            
            qb_z = qb_z + (-(V_z)/I_yy)*B_array[i,2]*B_array[i,1]
            qb_y = qb_y+ (-(V_y)/I_zz)*B_array[i,3]*B_array[i,0]
            ID=B_array[i,4]
            i=i+1
        
        
        #Move on to next cell or spar
        ID+=1
        
    return Qb_z, Qb_y

Qb_z=baseShearFlows(2,3,-30,20,B)[0]
Qb_y=baseShearFlows(2,3,-30,20,B)[1]

#Shear flow in the spar is constant
for i in range(len(Qb)):
    
    if Qb[i,2] == 3:
        Shear_Force_Spar_3 = Qb[i,1]

#Line_Integral_qb_3 = (qb_3*)/(t_sp*G)



    
    
