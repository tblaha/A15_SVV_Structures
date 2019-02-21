# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:00:45 2019

@author: Mathieu D'heer
"""

from UniversalConstants import *
from ReactionForces import *
import numpy as np
import matplotlib.pyplot as plt

d_yz_vec, Fx2, Fy, Fz, P_1 = sampleBendingShape([0], x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, 1e7, 5e8)

#Define a macauly function
    
def Macauly (x1, x2):
    a = x1 - x2
    if a < 0:
        a = 0
    else:
        a = 1
    return a 

def Macaulyyy (x1, x2):
    a = x1 - x2
    if a < 0:
        a = 0
    return a

def InternalShearForcex (xlocation):
    SFIx = 0
    return SFIx

def InternalShearForcey (xlocation):
    SFIy = (Macauly(xlocation,0)* xlocation * -q * cos(radians(theta))) + (Macauly(xlocation,x_h1) * -F_z_1) + (Macauly(xlocation,x_h2) * -F_z_2) + (Macauly(xlocation,x_h3) * -F_z_3) + (P_1 * Macauly(xlocation, x_h2 - d_a/2) * cos(theta)) - (P_2 * Macauly(xlocation, x_h2 + d_a/2) * cos(theta))
    return SFIy

def InternalShearForcez (xlocation):
    SFIz = (Macauly(xlocation,0)* xlocation * q * sin(radians(theta))) + (Macauly(xlocation,x_h1) * -F_z_1) + (Macauly(xlocation,x_h2) * -F_z_2) + (Macauly(xlocation,x_h3) * -F_z_3) + (P_1 * Macauly(xlocation, x_h2 - d_a/2) * sin(theta)) - (P_2 * Macauly(xlocation, x_h2 + d_a/2) * sin(theta))
    return SFIz



def InternalMomentx (xlocation):
    MIx = - (cos(radians(theta)) * q * (0.25*c_a - h_a/2) * xlocation/2) - (P_1 * cos(theta) * -h_a/2 * Macauly(xlocation, x_h2 - d_a/2)) + (P_1 * sin(theta) * Macauly(xlocation, x_h2 - d_a/2) * h_a/2) + (P_2 * cos(theta) * -h_a/2 * Macauly(xlocation, x_h2 - d_a/2)) - (P_2 * sin(theta) * Macauly(xlocation, x_h2 - d_a/2) * h_a/2) + F_z_1 * d_1 + F_z_3 * d_3   
    return MIx

def InternalMomenty (xlocation):
    MIy = (F_z_1 * Macaulyyy(xlocation,x_h1))  + (Macaulyyy(xlocation,x_h2) * F_z_2) + (Macaulyyy(xlocation,x_h3) * F_z_3) + (q * Macaulyyy(xlocation/2,0) * xlocation * cos(theta)) - (P_1* Macauly(xlocation, x_h2 - d_a/2) * cos(theta))  + (P_2 * Macauly(xlocation, x_h2 - d_a/2) * cos(theta))
    return MIy

def InternalMomentz (xlocation): 
    MIz = (F_y_1 * Macaulyyy(xlocation,x_h1)) + (Macaulyyy(xlocation,x_h2) * F_y_2) + (Macaulyyy(xlocation,x_h3) * F_y_3) + (q * Macaulyyy(xlocation/2,0) * xlocation * sin(theta)) + (P_1* Macauly(xlocation, x_h2 - d_a/2) * sin(theta))  - (P_2 * Macauly(xlocation, x_h2 - d_a/2) * sin(theta))
    return MIz