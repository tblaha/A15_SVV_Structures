# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:49:59 2019

@author: tblaha
"""

from UniversalConstants import *
import numpy as np


def zBending(x_h1, x_h2, x_h3, P_2, d_a, q, theta, l_a, d_1, d_3):
    # --- OUTPUTS ---
    # 
    
    # system of equations: (solution vector)
    # 
    # | F_1y | F_2y | F_3y | P_1 | c_1 | c_2 |
    
    np.cosd = lambda x : np.cos( np.deg2rad(x) )
    np.sind = lambda x : np.sin( np.deg2rad(x) )
    
    def genDispLine(x):
        const =              q*np.cosd(theta)*x**2/(3*2) \
                - (x > x_h1) * P_2*np.sind(theta)*(x - (x_h2 + d_a/2))**2/2
        avec  = np.array([-(x > x_h1) * (x - x_h1)**2/2,\
                          -(x > x_h2) * (x - x_h2)**2/2, \
                          -(x > x_h3) * (x - x_h3)**2/2, \
                          -(x > (x_h2-d_a/2)) * np.sind(theta) * (x - (x_h2-d_a/2))**2/2, \
                          x, \
                          1])
        return avec, const
    
    avec = np.zeros((6,6))
    bvec = np.zeros((6))
    
    # generate the linear equation vectors for the statics equations
    # sum of forces in y direction
    avec[0] = np.array([1,1,1,np.sind(theta), 0, 0])
    bvec[0] = q*np.cosd(theta)*l_a - np.sind(theta)*P_2
    
    # sum of moments around z
    avec[1] = np.array([x_h1,x_h2,x_h3,np.sind(theta)*(x_h2-d_a/2),0,0])
    bvec[1] = q*np.cosd(theta)*l_a**2/2 - np.sind(theta) * P_2*(x_h2+d_a/2)
    
    # hinge 1 condition
    avec[2],const = genDispLine(x_h1)
    bvec[2]       = -const + d_1
    
    # hinge 2 condition
    avec[3],const = genDispLine(x_h2)
    bvec[3]       = -const + 0
    
    # hinge 3 condition
    avec[4],const = genDispLine(x_h3)
    bvec[4]       = -const + d_3
    
    avec[5],const = genDispLine(x_h2-d_a/2)
    bvec[5]       = -const + 0
    
    return avec, bvec

avec, bvec = zBending(x_h1, x_h2, x_h3, p, d_a, q, theta, l_a, d_1, d_3)

x = np.linalg.solve(avec, bvec)

        
    
        
        
        
    

