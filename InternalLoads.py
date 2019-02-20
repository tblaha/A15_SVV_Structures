# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:00:45 2019

@author: Mathieu D'heer
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt

#Define a macauly function
def Macauly (x1, x2):
    a = x1 - x2
    if a < 0:
        a = 0 
    return a
    
def InternalShearForcez (xlocation):
    SFIz = Macauly(xlocation,0)* xlocation * q * sin(radians(theta)) + Macauly(xlocation,x_h1) * -F_z_1 + Macauly(xlocation,x_h2) * -F_z_2 + Macauly(xlocation,x_h3) * -F_z_3 + P_1 * Macauly(xlocation, x_h2 - d_a/2) * cos(theta) - P_2 * Macauly(xlocation, x_h2 - d_a/2) * cos(theta)
    return SFIz

def InternalShearForcey (xlocation):
    SFIy = Macauly(xlocation,0)* xlocation * -q * cos(radians(theta)) + Macauly(xlocation,x_h1) * -F_z_1 + Macauly(xlocation,x_h2) * -F_z_2 + Macauly(xlocation,x_h3) * -F_z_3 + P_1 * Macauly(xlocation, x_h2 - d_a/2) * sin(theta) - P_2 * Macauly(xlocation, x_h2 - d_a/2) * sin(theta)    
    return SFIy

def InternalMomentx (xlocation):
    MIx = cos(radians(theta)) * -q * (0.25*c_a - h_a/2) * Macauly(xlocation,0)* xlocation/2 + P_1 * cos(theta) * -h_a/2 * Macauly(xlocation, x_h2 - d_a/2)
    
    return


def InternalMomenty (A):
    
    
    return


def InternalMomentz (A):
    
    
    return