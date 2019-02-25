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
def MomentOfInertia(BoomDiscretization): 
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
#
##Used to verify the program
#A = np.array([[1,4,3,5] ,[1, 3, 5,2],[1, 6, 9,9] ,[1, 21, 9,1] ,[1, 6, 43, 6]])
#print(MomentOfInertia(A)) y z by bz
#A=np.array([[30,30,60,50],
#[-30,30,60,70],
#[50,90,80,30],
#[-50,-40,80,80]])
#print(MomentOfInertia(A))