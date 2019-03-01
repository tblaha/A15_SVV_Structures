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
theta=0     #Degrees (max) deflection,      26 Degrees
theta_radians=theta*(pi/180.) #Get theta in radians too
p=91700     #Force of actuator 2,           91.7kN
q=4.530     #Distributed aerodynamic load,  4.53kN/m
E=73.1e3    # Young's modulus Al 2042 T3    73.1GPa
G=28e3      # Shear modulus Aluminium       28GPa

#Stiffener properties
st_acc=1 #Change this to 1 to increase accuracy, 0 is to be
         #closer to analytical model
         
#A_st=(h_st+w_st-t_st*st_acc)*t_st 
w_st_a=w_st*t_st #Area of the wide piece of the stringer
h_st_a=h_st*t_st #Area of the wide piece of the stringer
w_st_d=t_st*0.5*st_acc #Centroid of the wide piece of the stringer
h_st_d=h_st*0.5 #Centroid of the tall piece of the stringer
A_st=h_st_a+w_st_a #Area of the stringer
AreaDistance_sum_st=h_st_a*h_st_d+w_st_a*w_st_d
Ybar_st=AreaDistance_sum_st/A_st

#Areas for shear flow calculations
#Rounded cell area
Cell_Area1=0.5*pi*(h_a/2)**2

#Cell with two diagonal parts
Cell_Area2=(c_a-(h_a/2))*(h_a/2)




