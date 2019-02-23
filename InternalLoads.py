# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:00:45 2019

@author: Mathieu D'heer, dverkooij
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt
#Getting the values for the reaction forces
#d_yz_vec, Fx2, Fy, Fz, P_1 = sampleBendingShape([0], x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, 13850069.95, 95733446.4887)

#Adapting the names of the reaction forces to this program


#Define a macauly function when 
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

def InternalShearForcex (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    SFIx = 0
    return SFIx

def InternalShearForcey (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    SFIy = (Macauly(xlocation,0)* xlocation * -q * cos(radians(theta)))\
            + (Macauly(xlocation,x_h1) * F_y_1) + (Macauly(xlocation,x_h2) * F_y_2)\
            + (Macauly(xlocation,x_h3) * F_y_3) + (P_1 * Macauly(xlocation, x_h2 - d_a/2) * sin(radians(theta))) \
            + (P_2 * Macauly(xlocation, x_h2 + d_a/2) * sin(radians(theta)))
    return SFIy

def InternalShearForcez (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    SFIz = (Macauly(xlocation,0)* xlocation * q * sin(radians(theta))) + (Macauly(xlocation,x_h1) * F_z_1)\
            + (Macauly(xlocation,x_h2) * F_z_2) + (Macauly(xlocation,x_h3) * F_z_3) \
            - (P_1 * Macauly(xlocation, x_h2 - d_a/2) * cos(radians(theta))) - (P_2 * Macauly(xlocation, x_h2 + d_a/2) * cos(radians(theta)))
    return SFIz



def InternalMomentx (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    MIx = - (cos(radians(theta)) * q * (0.25*c_a - h_a/2) * xlocation) \
          - (P_1 * cos(radians(theta)) * -h_a/2 * Macauly(xlocation, (x_h2 - d_a/2)))\
          + (P_1 * sin(radians(theta)) * Macauly(xlocation, x_h2 - d_a/2) * h_a/2) \
          + (P_2 * cos(radians(theta)) * -h_a/2 * Macauly(xlocation, x_h2 - d_a/2)) - \
          (P_2 * sin(radians(theta)) * Macauly(xlocation, x_h2 - d_a/2) * h_a/2) \
          + (F_z_1 * d_1 * Macauly(xlocation,x_h1)) + (F_z_3 * d_3 * Macauly(xlocation,x_h3))  
    return MIx

def InternalMomenty (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1):
    P_2 = p
    MIy = (F_z_1 * Macaulyyy(xlocation,x_h1))  + (Macaulyyy(xlocation,x_h2) * F_z_2) \
          + (Macaulyyy(xlocation,x_h3) * F_z_3) + (q * Macaulyyy(xlocation/2,0) * xlocation * cos(radians(theta)))\
          - (P_1* Macauly(xlocation, x_h2 - d_a/2) * cos(radians(theta)))  + (P_2 * Macauly(xlocation, x_h2 - d_a/2) * cos(radians(theta)))
    return MIy

def InternalMomentz (xlocation,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1): 
    P_2 = p
    MIz = (F_y_1 * Macaulyyy(xlocation,x_h1)) + (Macaulyyy(xlocation,x_h2) * F_y_2) + \
          (Macaulyyy(xlocation,x_h3) * F_y_3) + (q * Macaulyyy(xlocation/2,0) * xlocation * sin(radians(theta)))\
          + (P_1* Macauly(xlocation, x_h2 - d_a/2) * sin(radians(theta)))  - (P_2 * Macauly(xlocation, x_h2 - d_a/2) * sin(radians(theta)))
    return MIz

def getInternalLoads(xvec,Fx, Fy, Fz, P_1 ):
    Fx2=Fx
    F_y_1 = Fy[0]
    F_y_2 = Fy[1]
    F_y_3 = Fy[2]
    
#    F_y_1 = 5
#    F_y_2 = -2
#    F_y_3 = -3
    
    F_z_1 = Fz[0]
    F_z_2 = Fz[1]
    F_z_3 = Fz[2]
    SFIx=[]
    SFIy=[]
    SFIz=[]
    MIx=[]
    MIy=[]
    MIz=[]
    
    for i in xvec:
        SFIx.append(InternalShearForcex(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        SFIy.append(InternalShearForcey(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        SFIz.append(InternalShearForcez(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        MIx.append(InternalMomentx(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        MIy.append(InternalMomenty(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))
        MIz.append(InternalMomentz(i,F_y_1,F_y_2,F_y_3,F_z_1,F_z_2,F_z_3,Fx2,P_1))

    return SFIx, SFIy, SFIz, MIx, MIy, MIz

    
#def PlotDiagrams():
#    import matplotlib.pyplot as plt
#    x = np.arange(0,2771,0.1)
#    y1 = []
#    y2 = []
#    y3 = []
#    y4 = []
#    y5 = []
#    y6 = []
#    
#    for i in range(len(x)): 
#        y1.append(InternalShearForcex(x[i]))
#        i = +i 
#        
#    for i in range(len(x)): 
#        y2.append(InternalShearForcey(x[i]))
#        i = +i 
#        
#    for i in range(len(x)): 
#        y3.append(InternalShearForcez(x[i]))
#        i = +i 
#        
#    for i in range(len(x)): 
#        y4.append(InternalMomentx(x[i]))
#        i = +i 
#        
#    for i in range(len(x)): 
#        y5.append(InternalMomenty(x[i]))
#        i = +i 
#        
#    for i in range(len(x)): 
#        y6.append(InternalMomentz(x[i]))
#        i = +i 
#
#    #First row: plot 1-3
#    plt.subplot(231)
#    plt.plot(x,y1)
#    plt.title('Internal shear force x')
#    
#    plt.subplot(232)
#    plt.plot(x,y2)
#    plt.title('Internal shear foce y')
#    
#    plt.subplot(233)
#    plt.plot(x,y3)
#    #plt.axis([-2.*pi,2.*pi,-5.,5.]) # setting scale:xmin,xmax,ymin,ymax
#    plt.title('Internal shear force z')
#    
#    # Second row: plot 4-6
#    plt.subplot(234)
#    plt.plot(x,y4)
#    plt.title('Internal moment x')
#    
#    plt.subplot(235)
#    plt.plot(x,y5)
#    plt.title('Internal moment y')
#    
#    plt.subplot(236)
#    plt.plot(x,y6)
#    plt.title('Internal moment z')
#    
#    plt.show()
#
#
#
#
#
#
#
