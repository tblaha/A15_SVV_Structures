# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 16:42:48 2019

@author: daanv
"""

from numpy import genfromtxt

def getVerInternalLoads(case):
    vData = genfromtxt('verificationData.csv', delimiter=',')
    #vData looks like:
    #Row 1-Headers for load cases
    #Row 2-Headers for column
    #number, xcoord, [v_z, v_y, M_z, M_y, T]*3 (each load case) 
    #x in mm, forces in kN
    #case=0 for neutral, 1 for up, 2 for down
    x=vData[2:,1]
    vz=vData[2:,2+case*5]
    vy=vData[2:,3+case*5]
    mz=vData[2:,4+case*5]
    my=vData[2:,5+case*5]
    mx=vData[2:,6+case*5]
    return x,vz*1000,vy*1000,-mz*1000000,my*1000000,mx*1000000