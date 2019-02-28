# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:00:45 2019

@author: Mathieu D'heer, dverkooij
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt

#This program uses the EoMs in the report to find the internal force at any given
#point which can then be used to find the internal force diagrams.

#Define a macauly function to activate forces 
def Macauly (x1, x2):
    a = x1 - x2
    if a < 0:
        a = 0
    else:
        a = 1
    return a 

#Define a macauly function to activate forces and give them an arm
def Macaulyyy (x1, x2):
    a = x1 - x2
    if a < 0:
        a = 0
    return a 

#Calculation of the shear force in x in function of x coordinate
def InternalShearForcex (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    SFIx = 0
    return SFIx

#Calculation of the shear force in x in function of y coordinate
def InternalShearForcey (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    SFIy = (Macauly(xlocation,0)* xlocation * -q * cos(radians(theta)))\
            + (Macauly(xlocation,x_h1) * F_y_1) + (Macauly(xlocation,x_h2) * F_y_2)\
            + (Macauly(xlocation,x_h3) * F_y_3) + (P_1 * Macauly(xlocation, x_h2 - d_a/2) * sin(radians(theta))) \
            - (P_2 * Macauly(xlocation, x_h2 + d_a/2) * sin(radians(theta)))
    return SFIy

#Calculation of the shear force in z in function of x coordinate
def InternalShearForcez (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    SFIz = (Macauly(xlocation,0)* xlocation * q * sin(radians(theta))) + (Macauly(xlocation,x_h1) * F_z_1)\
            + (Macauly(xlocation,x_h2) * F_z_2) + (Macauly(xlocation,x_h3) * F_z_3) \
            + (P_1 * Macauly(xlocation, x_h2 - d_a/2) * cos(radians(theta))) - (P_2 * Macauly(xlocation, x_h2 + d_a/2) * cos(radians(theta)))
    return SFIz

#Calculation of the moment force in x in function of x coordinate
def InternalMomentx (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    MIx = - (cos(radians(theta)) * q * (0.25*c_a - h_a/2) * xlocation) \
          + (P_1 * cos(radians(theta)) * Macauly(xlocation, x_h2 - d_a/2) * h_a/2) \
          - (P_1 * sin(radians(theta)) * Macauly(xlocation, x_h2 - d_a/2) * h_a/2) \
          - (P_2 * cos(radians(theta)) * Macauly(xlocation, x_h2 + d_a/2) * h_a/2) \
          + (P_2 * sin(radians(theta)) * Macauly(xlocation, x_h2 + d_a/2) * h_a/2) \
#          + (F_z_1 * d_1 * Macauly(xlocation,x_h1)) + (F_z_3 * d_3 * Macauly(xlocation,x_h3))  
    return MIx

#Calculation of the moment force in y in function of x coordinate
def InternalMomenty (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    MIy = - (F_z_1 * Macaulyyy(xlocation, x_h1)) - (Macaulyyy(xlocation, x_h2)   * F_z_2) \
          - (Macaulyyy(xlocation,x_h3) * F_z_3)  - (q * Macaulyyy(xlocation/2,0) * xlocation * sin(radians(theta))) \
          - (P_1* Macaulyyy(xlocation, x_h2 - d_a/2) * cos(radians(theta)))  + (P_2 * Macaulyyy(xlocation, x_h2 + d_a/2) * cos(radians(theta)))
    return MIy


#Calculation of the moment force in z in function of x coordinate
def InternalMomentz (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1): 
    P_2 = p
    MIz = (F_y_1 * Macaulyyy(xlocation,x_h1)) + (Macaulyyy(xlocation,x_h2) * F_y_2) \
          + (Macaulyyy(xlocation,x_h3) * F_y_3) - (q * Macaulyyy(xlocation/2,0) * xlocation * cos(radians(theta)))\
          + (P_1* Macaulyyy(xlocation, x_h2 - d_a/2) * sin(radians(theta)))  - (P_2 * Macaulyyy(xlocation, x_h2 + d_a/2) * sin(radians(theta)))
    return MIz

#Calculation of the loads along the span extracting the forces from the reaction forces file. This is appened in a list. 
def getInternalLoads(xvec,Fx, Fy, Fz, P_1 ):
    #Convert input
    Fx2=Fx
    F_y_1 = Fy[0]
    F_y_2 = Fy[1]
    F_y_3 = Fy[2]

    F_z_1 = Fz[0]
    F_z_2 = Fz[1]
    F_z_3 = Fz[2]
    #Initialize lists
    SFIx=[]
    SFIy=[]
    SFIz=[]
    MIx=[]
    MIy=[]
    MIz=[]
    #Use all above functions for each position in X
    for i in xvec:
        SFIx.append(InternalShearForcex(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        SFIy.append(InternalShearForcey(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        SFIz.append(InternalShearForcez(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        MIx.append(InternalMomentx(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        MIy.append(InternalMomenty(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        MIz.append(InternalMomentz(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))

    return SFIx, SFIy, SFIz, MIx, MIy, MIz
