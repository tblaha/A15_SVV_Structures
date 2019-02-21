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
    SFIy = (Macauly(xlocation,0)* xlocation * -q * cos(radians(theta)))\
            + (Macauly(xlocation,x_h1) * -F_z_1) + (Macauly(xlocation,x_h2) * -F_z_2)\
            + (Macauly(xlocation,x_h3) * -F_z_3) + (P_1 * Macauly(xlocation, x_h2 - d_a/2) * cos(theta)) \
            - (P_2 * Macauly(xlocation, x_h2 + d_a/2) * cos(theta))
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

def PlotDiagrams():
    import matplotlib.pyplot as plt
    x = np.arange(0,2771,1)
    
    
    #First row: plot 1-3
    plt.subplot(231)
    plt.plot(x,y1)
    plt.title('Internal shear force x')
    
    plt.subplot(232)
    plt.plot(x,y2)
    plt.title('Internal shear foce y')
    
    plt.subplot(233)
    plt.plot(x,y3)
    #plt.axis([-2.*pi,2.*pi,-5.,5.]) # setting scale:xmin,xmax,ymin,ymax
    plt.title('Internal shear force z')
    
    # Second row: plot 4-6
    plt.subplot(234)
    plt.plot(x,y4)
    plt.title('Internal moment x')
    
    plt.subplot(235)
    plt.plot(x,y5)
    plt.title('Internal moment y')
    
    plt.subplot(236)
    plt.plot(x,y6)
    plt.title('Internal moment z')
    
    plt.show()
    
    return 0

PlotDiagrams()





