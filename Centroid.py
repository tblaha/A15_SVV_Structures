# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:18:19 2019

@author: daanv
"""


import UniversalConstants as UC
import math as m

#Calculated from the far right tip. Shifted to proper coordinate system in the 
#end. Proper coordinate system origin starts at spar.
#Furthermore it is important to note that only one half is considered.

#Equation to be used for z_bar is 
#(Sum of Area*Distance)/(Sum of Area)
Area_Sum=0 #Area
Area_Distance_Sum=0 #Area*Distance
Y_Bar=0

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
skin_Curved_Z=4*h/(m.pi*3)+(w)

#Add
Area_Sum+=skin_Curved_Area
Area_Distance_Sum+=skin_Area*skin_Curved_Z


#Stiffeners loose analysis
Area_st=(UC.w_st+UC.h_st)*UC.t_st
#Looking at stiffener like: _|_  
#z going left, y going up, zbar=0
#ybar calc:
Y_st_bar=((UC.w_st*UC.t_st)*(UC.t_st/2))/Area_st

#rotated to find Z from the T split for the rotated:
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


#the single 


#Add spar: 
z_sp=w
A_sp=UC.h_a*UC.t_sp

Area_Sum+=A_sp
Area_Distance_Sum+=A_sp*d_z_st

#Find Zbar and convert to proper coord system
Z_bar_wrong_coords=Area_Distance_Sum/Area_Sum
Z_bar=Z_bar_wrong_coords-w

print(Z_bar)



