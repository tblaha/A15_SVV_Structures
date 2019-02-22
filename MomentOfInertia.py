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
    #Define I_zz and I_yy
    I_zz = 0
    I_yy = 0
    i = 0 
    #Iterates over the amount of rows 
    for i in range((len((BoomDiscretization)))):
        #Formula moment of inertia. 
        I_zz = BoomDiscretization[i, UC.location_Bz] * (BoomDiscretization[i, UC.location_y]**2) + I_zz
        I_yy = BoomDiscretization[i, UC.location_By] * (BoomDiscretization[i, UC.location_z]**2) + I_yy
    return(I_zz, I_yy)
#
##Used to verificate the program
#A = np.array([[1,4,3,5] ,[1, 3, 5,2],[1, 6, 9,9] ,[1, 21, 9,1] ,[1, 6, 43, 6]])
#print(MomentOfInertia(A)) y z by bz
location_Bz = 3
location_By = 2
location_z = 1
location_y = 0
#A=np.array([[30,30,60,50],
#[-30,30,60,70],
#[50,90,80,30],
#[-50,-40,80,80]])
#print(MomentOfInertia(A))