# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:00:45 2019

@author: Mathieu D'heer
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt


def Macauly (xlocation, x1):
    a = x1 - xlocation
    if a < 0:
        a = 0 
        
    else:
        a = x1 - xlocation
        
    return a
print(Macauly(2,6))
    
def InternalShearForcey (xlocation):
    SFy = xlocation * q * sin(radians(theta)) 
    
    return

def InternalShearForcez (xlocation):
    
    
    return

def InternalMomentx (A):
    
    
    return


def InternalMomenty (A):
    
    
    return


def InternalMomentz (A):
    
    
    return