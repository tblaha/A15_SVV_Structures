# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:27:39 2019

@author: patri
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:57:40 2019

@author: patri
"""

import numpy as np
from UniversalConstants import *
##from discretization import *
#from Centroid import *
#from InternalLoads import *
#from Stiffeners import *

import matplotlib.pyplot as plt


def baseShearFlows(I_zz,I_yy,SFIz,SFIy,B_array,MIx,Z_bar):
 
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
    
    #geometry:
    h_a=225
    l_skin_curved=np.pi*(h_a/2.)    
    l_skin_2 = np.sqrt((c_a-h_a/2)**2+((h_a/2)**2))
    theta=0.253355
    #Create output arrays which will have the same number of rows as input boom area array
    Qb_z = np.zeros((len(B_array[:,0]),3))
    Qb_y = np.zeros((len(B_array[:,0]),3))
    
    #Array for y and z distances between the booms 
    B_Distance = np.zeros((len(B_array[:,0]),4))
    
    
    #Initialize first cell
    ID_current=1
    ID_new = 1
    
    #Looping across all the booms
    i=0
    
    #Do this for all 3 cells based on their IDs
    

    
    #Initialise all the moment contributions and line integrals to zero. Note moments are taken about the centroid
    #of the cross-section
    Moment_qb_z_1=0.
    Moment_qb_y_1=0.
    Moment_qb_z_2=0.
    Moment_qb_y_2=0.
    Moment_qb_y_3=0.
    
    Line_Integral_qb_1_z=0.
    Line_Integral_qb_1_y=0.
    Line_Integral_qb_2_z=0.
    Line_Integral_qb_2_y=0.
    Line_Integral_qb_3=0.    
    
    midpoints=np.zeros((len(B_array[:,0])+1,2))
     
    while ID_current<=3:
        
        #Initialize base shear at 0 in each cell as this will start from the
        #point of the cut
        qb_z=0
        qb_y=0
        
    
        #Do this until new cell/spar

        
        while ID_current==ID_new:
           
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
            
            #Distance between each boom. 
            #FORMAT: / i number / y-direction / z-direction / ID /
            if i==len(B_array[:,0])-1:
                B_Distance[i,2]=0.
               
            else:
                B_Distance[i+1,1]=abs(B_array[i+1,0]-B_array[i,0])
                B_Distance[i+1,2]=abs(B_array[i+1,1]-B_array[i,1])
                midpoint_y=(B_array[i+1,0]+B_array[i,0])/2.
                midpoint_z=(B_array[i+1,1]+B_array[i,1])/2.
                midpoints[i+1,0]=midpoint_y
                midpoints[i+1,1]=midpoint_z
                
            
            #Distance to centroid is moment arm:
            moment_arm=np.sqrt((midpoints[i,0])**2+((midpoints[i,1]-Z_bar)**2))
            #print ("Moment arm is", moment_arm)
            
            
            #Pythagorean distance along which each q acts
            Mult_Dist = np.sqrt((B_Distance[i,1]**2)+(B_Distance[i,2]**2))
          
            
            
            if (ID_current == 1):
                Line_Integral_qb_1_y=Line_Integral_qb_1_y + np.multiply(Mult_Dist,Qb_y[i,1])/t_sk
                Line_Integral_qb_1_z=Line_Integral_qb_1_z + np.multiply(Mult_Dist,Qb_z[i,1])/t_sk
                
                #Moment
                #print(moment_arm)
                Moment_qb_y_1=Moment_qb_y_1 + Qb_y[i,1]*moment_arm
                Moment_qb_z_1=Moment_qb_z_1 + Qb_z[i,1]*moment_arm
                
            
                
            elif (ID_current == 2):
                moment_arm_z=abs(B_array[i,0])
                moment_arm_y=abs(B_array[i,1]-Z_bar)
                Line_Integral_qb_2_y=Line_Integral_qb_2_y + (np.multiply(Mult_Dist,Qb_y[i,1]))/t_sk
                Line_Integral_qb_2_z=Line_Integral_qb_2_z + (np.multiply(Mult_Dist,Qb_z[i,1]))/t_sk
                
               #Moment
                Moment_qb_y_2=Moment_qb_y_2 + Qb_y[i,1]*np.cos(theta)*moment_arm_z+Qb_y[i,1]*np.sin(theta)*moment_arm_y
                Moment_qb_z_2=Moment_qb_z_2 + Qb_z[i,1]*np.cos(theta)*moment_arm_z+Qb_z[i,1]*np.sin(theta)*moment_arm_y
                
                
            
                
            elif (ID_current == 3):
                
                moment_arm_y = abs(B_array[i,1]-Z_bar)
                
                Line_Integral_qb_3=Line_Integral_qb_3 + (np.multiply(Mult_Dist,Qb_y[i,1]))/t_sp    
                
                #Moment Contribution
                Moment_qb_y_3=Moment_qb_y_3+Qb_y[i,1]*moment_arm_y
            
            #Note2: The area in B_array in y-direc and z-direc is almost the same
            qb_z = qb_z + (-(SFIz)/I_yy)*B_array[i,2]*B_array[i,1]
            qb_y = qb_y+ (-(SFIy)/I_zz)*B_array[i,3]*B_array[i,0]
           
            i=i+1
            if i==len(B_array[:,0]):
                break
            ID_new=B_array[i,4]
           
        
        #Move on to next cell or spar
        ID_current+=1
    
    
        
        
    #Moment contribution from the constant shears:
    #Moment_Cont_qs0_1=2*Cell_Area1*qs0_1
    #Moment_Cont_qs0_2=2*Cell_Area_2*qs0_2
    
    #If centroid lies to right of hinge, then the shear force in y will create a negative moment
    if Z_bar<0:
        SFIy=-SFIy
        Moment_qb_y_3=-Moment_qb_y_3
        
    
    #Total moment contribution including base shear
    RHS_Moment_eq=Moment_qb_y_1 + Moment_qb_y_2 - Moment_qb_y_3 + Moment_qb_z_1 + Moment_qb_z_2
    
    #Note: No moment caused by SFIz as moments taken about the centroid
    
   
   
    External_Loads = MIx + SFIy*(abs(Z_bar))
    
    #Matrix Solving coefficients 
    A_11 = (1./(2.*Cell_Area1))*(((l_skin_curved)/(t_sk))+((h_a/(t_sp))))
    A_12 = -(1./(2.*Cell_Area1))*((h_a)/(t_sp))    
    A_21 = -(1./(2.*Cell_Area2))*((h_a)/(t_sp))
    A_22 = (1./(2.*Cell_Area2))*(((l_skin_2)/(t_sk))+((h_a/(t_sp))))
    A_31=2*Cell_Area1
    A_32=2*Cell_Area2
    
    B_1=-(1./(2.*Cell_Area1))*(Line_Integral_qb_1_y+Line_Integral_qb_1_z-Line_Integral_qb_3)
    B_2=-(1./(2.*Cell_Area2))*(Line_Integral_qb_2_y+Line_Integral_qb_2_z+Line_Integral_qb_3)
    B_3=External_Loads-RHS_Moment_eq
    
    A = np.array([[A_11, A_12, -1],[A_21,A_22,-1],[A_31,A_32,0]])
    b = np.array([[B_1],[B_2],[B_3]])
    
    #Solve and output vector x[qs0_1,qs0_2,qs0_3]
    x = np.linalg.solve(A,b)
    
    #Function for superiposing the constant shear flows with the final shear flows
    
    def getFinalShearFlow():
        #2D array with final shear flows:
        
        Shear_Final = np.zeros((len(B_array[:,0]),2))
        
        for i in range(len(B_array[:,0])):
            Shear_Final[i,0]=i+1
            if B_array[i,4]==1:
                Shear_Final[i,1]=Qb_y[i,1]+Qb_z[i,1]+x[0]
            
            elif B_array[i,4]==2:
                Shear_Final[i,1]=Qb_y[i,1]+Qb_z[i,1]+x[1]
        
            else:
                Shear_Final[i,1]=Qb_y[i,1]+Qb_z[i,1]+x[1]-x[0]

        return Shear_Final
            
    Shear_Final=getFinalShearFlow()
        
    return Qb_z, Qb_y,B_Distance,Line_Integral_qb_3,A,b,x,Shear_Final