# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:49:34 2019

@author: Mathieu D'heer
"""
#Import neccesary modules
import UniversalConstants as UC
from math import *
import numpy as np
#Define constants


def MomentOfInertia(BoomDiscretization): 
    I_zz = 0
    I_yy = 0
    i = 0 
    for i in range((len((BoomDiscretization)))):
        I_zz = BoomDiscretization[i, UC.location_Bz] * BoomDiscretization[i, UC.location_y]**2 + I_zz
        I_yy = BoomDiscretization[i, UC.location_By] * BoomDiscretization[i, UC.location_z]**2 + I_yy
        i =+i
    return(I_zz, I_yy)

A = np.array([[1,4,3,5] ,[1, 3, 5,2],[1, 6, 9,9] ,[1, 21, 9,1] ,[1, 6, 43, 6]])
print(MomentOfInertia(A))
