# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:18:19 2019

@author: daanv
"""


import UniversalConstants as UC
import math as m
    
def findCentroid():
    #Returns Y_bar,Z_bar,Z_bar_tip
    #Calculated from the far right tip. Shifted to proper coordinate system in the 
    #end. Proper coordinate system origin starts at spar.
    #Furthermore it is important to note that only top half is considered.
    
    Y_bar=0
    
    #Equation to be used for z_bar is 
    #(Sum of Area*Distance)/(Sum of Area)
    Area_Sum=0 #Area
    Area_Distance_Sum=0 #Area*Distance
    
    #First find angle between z axis and the diagonal part.
    h=UC.h_a / 2 #also r
    w=UC.c_a-h
    angle=m.atan(h/w)
    
    #Seperate parts
    #Skin straight section geo properties
    l_Skin_Straight=m.sqrt(h**2+w**2)
    skin_Area=UC.t_sk*l_Skin_Straight
    #Find location of centre of section wrt hinge line
    skin_Straight_Z=(l_Skin_Straight/2)*(m.cos(angle))
    
    #Add
    Area_Sum+=skin_Area
    Area_Distance_Sum+=skin_Area*skin_Straight_Z
    
    #Skin Curved section
    #Find Length of section
    #Circumference is 2pi*r
    l_Skin_Curved=2*m.pi*h/4
    skin_Curved_Area=l_Skin_Curved*UC.t_sk
    #Quarter-circular area centroid is 4r/3pi
    skin_Curved_Z=(4*h/(m.pi*3))+(w)
    
    #Add
    Area_Sum+=skin_Curved_Area
    Area_Distance_Sum+=skin_Area*skin_Curved_Z
    
    #=========================
    #Stiffeners loose analysis
    #=========================
    Area_st=(UC.w_st+UC.h_st)*UC.t_st
    #Looking at stiffener like: _|_  
    #z going left, y going up, zbar=0
    #ybar calc:
    Y_st_bar=((UC.w_st*UC.t_st)*(UC.t_st/2))/Area_st
    
    #rotated to find Z from the T split for the rotated position:
    Z_st_bar=Y_st_bar*m.sin(angle)
    #Stiffeners distributed equally over straight part of skin. 
    #N_st=17, 7 on skin part, 9 segments Stiffener spacing: 
    #Distance over straight skin between stiffeners
    d_st=l_Skin_Straight/9
    #iterate over stiffeners
    i=1
    for q in range(7):
        #distance is Zfrom stiffener centre + distance to stiffener centre
        d_z_st=Z_st_bar+d_st*i
        
        #add
        Area_Sum+=Area_st
        Area_Distance_Sum+=d_z_st*Area_st
        #increase iterator
        i+=1
    
    
    #the 45 degree stiffener on the curved edge:
    #First to the spar, then to the z location of the split point, then back to centroid
    Z_st_rot_bar=w+h*0.5*m.sqrt(2)-Y_st_bar*0.5*m.sqrt(2)
    #add
    Area_Sum+=Area_st
    Area_Distance_Sum+=Z_st_rot_bar*Area_st
    
    #the 90 deg stiffener on the tip of the curved edge
    #Half area because considering half stiffener
    Z_st_straight_bar=UC.c_a-Y_st_bar
    #add
    Area_Sum+=Area_st*0.5
    Area_Distance_Sum+=Z_st_straight_bar*Area_st*0.5
    
    #Add spar: 
    Z_sp=w
    A_sp=UC.h_a*UC.t_sp
    
    Area_Sum+=A_sp
    Area_Distance_Sum+=A_sp*Z_sp
    
    #Find Zbar and convert to proper coord system
    Z_bar_tip=Area_Distance_Sum/Area_Sum
    Z_bar=Z_bar_tip-w
    
    #output
    return Y_bar,Z_bar,Z_bar_tip
