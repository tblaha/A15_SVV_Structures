# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:33:40 2019

@author: daanv
"""

from numpy import genfromtxt

def getVerDeflections(case):
#   Row 1 Text
#   Row 2 Case def, neutral 0 , up1, down 2
#   Headers - X, [Le_z,Le_y,Te_z,Te_y]*3    
    vData = genfromtxt('TotalDeflections.csv', delimiter=',')
    x=vData[3:,0]
    LE_Z=vData[3:,1+case*4]
    LE_Y=vData[3:,2+case*4]
    TE_Z=vData[3:,3+case*4]
    TE_Y=vData[3:,4+case*4]
    return x,LE_Z,LE_Y,TE_Z,TE_Y