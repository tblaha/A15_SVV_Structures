# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:18:19 2019

@author: daanv
"""


import UniversalConstants as UC
import math as m
    
    
def findCentroid():
    #Returns Y_bar,Z_bar,Z_bar_tip
    #Calculated for the hinge
    #Furthermore it is important to note that only top half is considered.
    #Stiffeners are point areas since adding the stiffeners'centroid would only
    #make a difference of less than 0.001mm
    Y_bar=0
    
    #Equation to be used for z_bar is 
    #(Sum of Area*Distance)/(Sum of Area)
    Area_Sum=0 #Area
    Area_Distance_Sum=0 #Area*Distance
    
    #First find some additional geom properties
    h=UC.h_a / 2 #also r
    w=UC.c_a-h
    
    #Seperate parts
    #Skin straight section geo properties
    l_Skin_Straight=m.sqrt(h**2+w**2)
    skin_Area=UC.t_sk*l_Skin_Straight
    #Find location of centre of section wrt hinge line
    skin_Straight_Z=-w/2
    
    #Add
    Area_Sum+=skin_Area
    Area_Distance_Sum+=skin_Area*skin_Straight_Z
    
    #Skin Curved section
    #Find Length of section
    #Circumference is 2pi*r
    l_Skin_Curved=2*m.pi*h/4
    skin_Curved_Area=l_Skin_Curved*UC.t_sk
    
    #Quarter-circular area centroid is 4r/3pi
    skin_Curved_Z=(4*h/(m.pi*3))
    
    #Add
    Area_Sum+=skin_Curved_Area
    Area_Distance_Sum+=skin_Area*skin_Curved_Z
    
    #=========================
    #Stiffeners separate analysis
    #=========================
    Area_st=(UC.w_st+UC.h_st)*UC.t_st
    #Stiffeners distributed equally over straight part of skin. 
    #N_st=17, 7 on skin part, 8 segments Stiffener spacing (edges is half): 
    d_st=w/8
    #iterate over stiffeners
    for i in range(7):
        #distance is Zfrom stiffener centre + distance to stiffener centre
        d_z_st=-d_st*(i+0.5)
        #add
        Area_Sum+=Area_st
        Area_Distance_Sum+=d_z_st*Area_st
    
    
    #the 45 degree stiffener on the curved edge:
    #First to the spar, then to the z location of the split point, then back to centroid
    Z_st_rot_bar=h*0.5*m.sqrt(2)
    #add
    Area_Sum+=Area_st
    Area_Distance_Sum+=Z_st_rot_bar*Area_st
    
    #the 90 deg stiffener on the tip of the curved edge
    #Half area because considering half of a stiffener
    Z_st_straight_bar=h
    #add
    Area_Sum+=Area_st*0.5
    Area_Distance_Sum+=Z_st_straight_bar*Area_st*0.5
    
    #Add spar, half since only half spar is in the top area: 
    Z_sp=0
    A_sp=UC.h_a*UC.t_sp*0.5
    
    Area_Sum+=A_sp
    Area_Distance_Sum+=A_sp*Z_sp
    
    #Find Zbar 
    Z_bar=Area_Distance_Sum/Area_Sum
    
    #output
    return Y_bar,Z_bar,l_Skin_Curved
