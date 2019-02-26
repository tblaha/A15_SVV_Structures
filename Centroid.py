# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:18:19 2019

@author: daanv
"""


import UniversalConstants as UC
import math as m
import numpy as np

def findCentroid(stiffeners):
    #Returns Y_bar,Z_bar,Z_bar_tip
    #Calculated for the hinge
    #Input is 2D numpy array having [y [mm], z[mm], area[mm2]] 
    #Area being 1 for being to the left of the spar, 2 for being to the right
    #Stiffeners coordinates are origins of the centroids.
    Y_bar=0

    #Equation to be used for z_bar is 
    #(Sum of Area*Distance)/(Sum of Area)
    Area_Sum=0 #Area
    Area_Distance_Sum=0 #Area*Distance
    
    #First find some additional geom properties
    h=UC.h_a / 2 #also r
    w=UC.c_a-h
    
    #Seperate parts
    #Add spar 
    Z_sp=0
    A_sp=UC.h_a*UC.t_sp
    
    Area_Sum+=A_sp
    Area_Distance_Sum+=A_sp*Z_sp
    
    #Skin straight section geo properties
    l_Skin_Straight=m.sqrt(h**2+w**2)
    skin_Area=UC.t_sk*l_Skin_Straight
    #Find location of centre of section wrt hinge line
    skin_Straight_Z=-w/2
    
    #Add (Twice, since part exists twice at same z location)
    Area_Sum+=skin_Area*2
    Area_Distance_Sum+=skin_Area*skin_Straight_Z*2
    
    #Skin Curved section
    #Find Length of section
    #Circumference is 2pi*r
    l_Skin_Curved=m.pi*h
    skin_Curved_Area=l_Skin_Curved*UC.t_sk
    
    #Semi-circular area centroid is 4r/3pi
    skin_Curved_Z=(4*h)/(m.pi*3)
    
    #    Add
    Area_Sum+=(skin_Curved_Area)
    Area_Distance_Sum+=(skin_Curved_Area*skin_Curved_Z)

    #=========================
    #Stiffeners
    #=========================
    
    for i in range(len(stiffeners)):
        z_st=stiffeners[i][1]
        Area_Sum+=UC.A_st
        Area_Distance_Sum+=UC.A_st*z_st
        
    #Find Zbar 
    Z_bar=Area_Distance_Sum/Area_Sum
    
    #output
    return Y_bar,Z_bar

#Verifcation data
#Stiffeners=[[ 109.71864543,  24.86099043,    1.        ],
# [  70.21178169,   87.90082885,    1.        ],
# [   0.,          112.5,           1.        ],
# [ -70.21178169,   87.90082885,    1.        ],
# [-109.71864543,   24.86099043,    1.        ],
# [ -99.77801022,  -49.13515163,    2.        ],
# [ -80.77267494, -122.53797989,    2.        ],
# [ -61.76733966, -195.94080815,    2.        ],
# [ -42.76200438, -269.34363641,    2.        ],
# [ -23.7566691,  -342.74646467,    2.        ],
# [  -4.75133382, -416.14929293,    2.        ],
# [   4.75133382, -416.14929293,    2.        ],
# [  23.7566691,  -342.74646467,    2.        ],
# [  42.76200438, -269.34363641,    2.        ],
# [  61.76733966, -195.94080815,    2.        ],
# [  80.77267494, -122.53797989,    2.        ],
# [  99.77801022,  -49.13515163,    2.        ]]
#NoStiffeners=[[]]
#EasyStiffeners=[[0,-50,0],
#        [0,-200,0]]
#print(findCentroid(EasyStiffeners))