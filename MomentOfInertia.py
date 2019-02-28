# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:49:34 2019

@author: Mathieu D'heer
"""
#Import neccesary modules
import UniversalConstants as UC
from math import *
import numpy as np

#Start Definition
def momentOfInertia(BoomDiscretization): 
    #Boom_disc array is [y,z,By,Bz]
    #Define I_zz and I_yy
    I_zz = 0
    I_yy = 0
    i = 0 
    #Iterates over the amount of rows 
    for i in range((len((BoomDiscretization)))):
        #Formula moment of inertia. 
        I_zz += BoomDiscretization[i, 3] * (BoomDiscretization[i, 0]**2)
        I_yy += BoomDiscretization[i, 2] * (BoomDiscretization[i, 1]**2)
    return(I_zz, I_yy)
