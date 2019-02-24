# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:04:53 2019

@author: daanv
"""
from math import *
#All in mm, N, N/mm, N/mm^2, Deg
c_a=547     #Chord Length Aileron,          0.547m
l_a=2771    #Length of the aileron,         2.771m
x_h1=153    #X-pos Hinge 1,                 0.153m
x_h2=1281   #X-pos Hinge 2,                 1.281m
x_h3=2681   #X-pos Hinge 3,                 2.681m
d_a=280     #Distance between actuators,    28cm
h_a=225     #Height Aileron,                22.5cm
t_sk=1.1    #Thickness Skin,                1.1mm
t_sp=2.9    #Thickness Spar,                2.9mm
t_st=1.2    #Thickness Stiffener,           1.2mm
h_st=15     #Height Stiffener,              1.5cm
w_st=20     #Width Stiffener,               2cm
n_st=17     #Number of Stiffeners,          17
d_1=11.03   #Vertical displacement hinge 1, 1.103cm
d_3=16.42   #Vertical displacement hinge 3, 1.642cm
theta=26    #Degrees max deflection,        26
p=91700     #Force of actuator 2,           91.7kN
q=4.530     #Distributed aerodynamic load,  4.53kN/m
#E=69e3      # Young's modulus Aluminium     69GPa
E=73.1e3      # Young's modulus Aluminium 2024T3
G=28e3      # Shear modulus Aluminium     28GPa
A_st=(h_st+w_st-t_st)*t_st

#Rounded cell
Cell_Area1=0.5*pi*(h_a/2)**2
#Cell with two diagonal parts
Cell_Area2=(c_a-(h_a/2))*(h_a/2)

#Module specific: 

#################Module 1#################
#Centroid.py
#centroid defined as Z_bar, Y_bar=0
#Z_bar is from hinge line
#findCentroid() #Returns Y_bar,Z_bar

#################Module 2#################
#discretization.py
#discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, nodes_between=50,ec=0.0001,offset=30)
#discretizes the span with concentrations of nodes around points of interest

#################Module 3#################
#MomentOfInertia.py
#Moment of inertia is defined as I_zz and I_yy
#Output is given as a (I_zz, I_yy)
#The variables underneath give the placement of the boom area and the distance of that boom area in the discretization matrix
location_Bz = 3
location_By = 2
location_z = 1
location_y = 0


#################Module 4#################




#################Module 5#################



#################Module 6#################



#################Module 7#################



#################Module 8#################