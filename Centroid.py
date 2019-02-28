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
    #Sp=Spar, Sk=Skin, St=Stiffener. Useful abbreviations
    Y_bar=0

    #Equation to be used for z_bar is 
    #(Sum of Area*Distance)/(Sum of Area)
    #Set up the variables to be used
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
    
    #Add to the sums
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
