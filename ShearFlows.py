# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:57:40 2019

@author: patri
"""

import numpy as np
from UniversalConstants import *
from discretization import *
from Centroid import *
from InternalLoads import *
from Stiffeners import *

import matplotlib.pyplot as plt

MIx=InternalMomentx(0)
stiffeners = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp)
Y_bar,Z_bar=findCentroid(stiffeners)
B=discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, Y_bar, Z_bar, 3)

#First find some additional geom properties
h=UC.h_a / 2 #also r
l_Skin_Curved=m.pi*h
Z_Hingeline=UC.c_a-h

def baseShearFlows(I_zz,I_yy,SFIz,SFIy,B_array,l_Skin_Curved,MIx,Z_Hingeline,Z_bar):
    #This function takes in the MOI parmeters as well as internal shear forces and 
    #cross sectional boom discretization.
    #The output is a 2D array with all the base shear flows in each segment
    #
    #---INPUTS---#
    #I_zz                : MOI about z axis
    #I_yy                : MOI about y axis
    #V_z                 : Internal shear foce in z direction
    #V_y                 : Internal shear force in y direction
    #B_Array:
    #2D array from disretization function which looks like:
     # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # cell id: 1 (exclusively left cell, anticlockwise sorted)
    #          2 (exclusively right cell, clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    #
    #---OUTPUTS---#
    #The output will be a 2D numpy array (Qb) with the numbered shear flows:
    #| q_i number | value |
    
    #Note q1 will be the represent the shear flow between boom 0 and 1 and so on
    
    #Create output arrays which will have the same number of rows as input boom area array
    Qb_z = np.zeros((len(B_array[:,0]),3))
    Qb_y = np.zeros((len(B_array[:,0]),3))
    
    B_Distance = np.zeros((len(B_array[:,0]),4))
    
    Line_Integral_qb = np.zeros((len(B_array[:,0]),4))
    
    Moment_Integral_qb = np.zeros((len(B_array[:,0]),4))
    
    #Initialize first cell
    ID_current=1
    ID_new = 1
    
    #Looping across all the booms
    i=0
    
    #Do this for all 3 cells based on their IDs
    

    
    #Initialise all the moment contributions and line integrals to zero. Note moments are taken about the centroid
    #of the cross-section
    Moment_Cont_qb_1_z=0.
    Moment_Cont_qb_1_y=0.
    Moment_Cont_qb_2_z=0.
    Moment_Cont_qb_2_y=0.
    Moment_Cont_qb_3=0.
    
    Line_Integral_qb_1=0.
    Line_Integral_qb_2=0.
    Line_Integral_qb_3=0.    
    
    while ID_current<=3:
        
        #Initialize base shear at 0 in each cell as this will start from the
        #point of the cut
        qb_z=0
        qb_y=0
        
    
        #Do this until new cell/spar

        
        while ID_current==ID_new:
            if i==len(B_array[:,0])-1:
                break
            #Update Qb_z
            Qb_z[i,0]=i+1
            Qb_z[i,1]=qb_z
            Qb_z[i,2]=ID_current
            
            #Update Qb_y
            Qb_y[i,0]=i+1
            Qb_y[i,1]=qb_y
            Qb_y[i,2]=ID_current
            
            #Update B_Distance
            B_Distance[i,0]=i+1
            B_Distance[i,3]=ID_current
            
            #Update Line integral q_b
            Line_Integral_qb[i,0]=i+1
            Line_Integral_qb[i,3]=ID_current
            
            #Updare Moment integral q_b:
            Moment_Integral_qb[i,0]=i+1
            Moment_Integral_qb[i,3]=ID_current
            
            #Distance between each boom. 
            #FORMAT: / i number / y-direction / z-direction / ID /
            
            if i==len(B_array[:,0]):
                break
            
            B_Distance[i,1]=abs(B_array[i+1,0]-B_array[i,0])
            B_Distance[i,2]=abs(B_array[i+1,1]-B_array[i,1])
            
            #Line Integral q_b in cell 1.
            #Formula used: (q_b*Length)/(t_skin*G)
            #FORMAT: / i number / q_b_y / q_b_z / ID /
            #if statement: when the ID is equal to 1 or 2, we use t_skin. when ID is equal to 3, then we should use t_spar.
            #I summed up the line integral shear flows for skin 1, skin 2 and spar 3 (old value + q_b_y + q_b_z).
            if (ID_current == 1):
                Line_Integral_qb[i,1] = (np.multiply(Qb_y[i,1],B_Distance[i,1]))/(t_sk*G)
                Line_Integral_qb[i,2] = (np.multiply(Qb_z[i,1],B_Distance[i,2]))/(t_sk*G)
                
                Moment_Integral_qb[i,1]=(np.multiply(Qb_y[i,1],B_Distance[i,1]))
                Moment_Integral_qb[i,1]=(np.multiply(Moment_Integral_qb[i,1],B_Distance[i,2]))
                
                Moment_Integral_qb[i,2]=(np.multiply(Qb_z[i,1],B_Distance[i,2]))
                Moment_Integral_qb[i,2]=(np.multiply(Moment_Integral_qb[i,2],B_Distance[i,1]))
                
                #Moment contribution will be negative for first skin
                Moment_Cont_qb_1_z= -(Moment_Cont_qb_1_z+ Moment_Integral_qb[i,2])
                Moment_Cont_qb_1_y= -(Moment_Cont_qb_1_y + Moment_Integral_qb[i,1])
                
                Line_Integral_qb_1 = Line_Integral_qb_1 + Line_Integral_qb[i,1] + Line_Integral_qb[i,2]  
                
            
                
            elif (ID_current == 2):
                Line_Integral_qb[i,1] = (np.multiply(Qb_y[i,1],B_Distance[i,1]))/(t_sk*G)
                Line_Integral_qb[i,2] = (np.multiply(Qb_z[i,1],B_Distance[i,2]))/(t_sk*G)
                
                Moment_Integral_qb[i,1]=(np.multiply(Qb_y[i,1],B_Distance[i,1]))
                Moment_Integral_qb[i,1]=(np.multiply(Moment_Integral_qb[i,1],B_Distance[i,2]))
                
                Moment_Integral_qb[i,2]=(np.multiply(Qb_z[i,1],B_Distance[i,2]))
                Moment_Integral_qb[i,2]=(np.multiply(Moment_Integral_qb[i,2],B_Distance[i,1]))
                
                #Moment contribution is positive for the second skin
                Moment_Cont_qb_2_z= Moment_Cont_qb_2_z+ Moment_Integral_qb[i,2]
                Moment_Cont_qb_2_y= Moment_Cont_qb_2_y + Moment_Integral_qb[i,1]
                
                Line_Integral_qb_2 = Line_Integral_qb_2 + Line_Integral_qb[i,1] + Line_Integral_qb[i,2]  
            
                
            elif (ID_current == 3):
                Line_Integral_qb[i,1] = (np.multiply(Qb_y[i,1],B_Distance[i,1]))/(t_sp*G)
                Line_Integral_qb[i,2] = (np.multiply(Qb_z[i,1],B_Distance[i,2]))/(t_sp*G)
                
                Moment_Integral_qb[i,1]=(np.multiply(Qb_y[i,1],B_Distance[i,1]))
                Moment_Integral_qb[i,1]=(np.multiply(Moment_Integral_qb[i,1],B_Distance[i,2]))
                
                #Moment contribution is negative for spar 
                Moment_Cont_qb_3 =  -(Moment_Cont_qb_3+Moment_Integral_qb[i,1])
                Line_Integral_qb_3 = Line_Integral_qb_3 + Line_Integral_qb[i,1] + Line_Integral_qb[i,2]
            
            i=i+1
            qb_z = qb_z + (-(SFIz)/I_yy)*B_array[i,2]*-B_array[i,1]
            qb_y = qb_y+ (-(SFIy)/I_zz)*B_array[i,3]*-B_array[i,0]
            ID_new=B_array[i,4]
            
            
            
        
        #Move on to next cell or spar
        ID_current+=1
        
    
    

    #Moment contribution from the constant shears:
    #Moment_Cont_qs0_1=2*Cell_Area1*qs0_1
    #Moment_Cont_qs0_2=2*Cell_Area_2*qs0_2
    
    #Total moment contribution including base shear
    RHS_Moment_eq=Moment_Cont_qb_1_z +  Moment_Cont_qb_1_y + Moment_Cont_qb_2_z + Moment_Cont_qb_2_y + Moment_Cont_qb_3 
    
    External_Loads = MIx - SFIy*(abs(Z_Hingeline-Z_bar))
    
    #Matrix Solving coefficients 
    A_11 = (1./(2.*Cell_Area1))*(((l_Skin_Curved)/(t_sk*G))+((h_a/(t_sp*G))))
    A_12 = -(1./(2.*Cell_Area1))*((h_a)/(t_sp*G))    
    A_21 = -(1./(2.*Cell_Area2))*((h_a)/(t_sp*G))
    A_22 = (1./(2.*Cell_Area2))*(((l_Skin_Curved)/(t_sk*G))+((h_a/(t_sp*G))))
    A_31=2*Cell_Area1
    A_32=2*Cell_Area2
    
    B_1=-(1./(2.*Cell_Area1))*(Line_Integral_qb_1+Line_Integral_qb_3)
    B_2=-(1./(2.*Cell_Area2))*(Line_Integral_qb_2+Line_Integral_qb_3)
    B_3=External_Loads-RHS_Moment_eq
    
    A = np.array([[A_11, A_12, -1],[A_21,A_22,-1],[A_31,A_32,0]])
    b = np.array([[B_1],[B_2],[B_3]])
    
    x = np.linalg.solve(A,b)
    return Qb_z, Qb_y,B_Distance,Line_Integral_qb,Line_Integral_qb_1,Line_Integral_qb_2,Line_Integral_qb_3,A,b,x


    #Takes in light integral of base shear and solves for angle of twist as well
    #as final total shear
    
    

Qb_z=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[0]
Qb_y=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[1]
B_Distance=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[2]
Line_Integral_qb=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[3]
Line_Integral_qb_1=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[4]
Line_Integral_qb_2=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[5]
Line_Integral_qb_3=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[6]
A=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[7]
b=baseShearFlows(23,528,30,20,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[8]


#Input: I_zz[mm^4],I_yy[],SFIz,SFIy,B_array,l_Skin_Curved,MIx,Z_Hingeline,Z_bar
#Output:Constant / shear flow in cell 1 / Constant shear flow in cell 2 / dtheta/dz /
x=baseShearFlows(13850069.95,95733446.48,3425*10**3,2000*10**3,B,l_Skin_Curved,MIx,Z_Hingeline,Z_bar)[9] 