# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:49:59 2019

@author: tblaha
"""

from UniversalConstants import *
import numpy as np

def getDispCoefficients_z(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta):
    const =              q*np.cosd(theta)*1/(4*3*2)*x**4 \
            - int((x > (x_h2 + d_a/2))) * P_2*np.sind(theta)*1/(3*2)*(x - (x_h2 + d_a/2))**3
    avec  = np.array([-int((x > x_h1)) * 1/(3*2) * (x - x_h1)**3,\
                      -int((x > x_h2)) * 1/(3*2) * (x - x_h2)**3, \
                      -int((x > x_h3)) * 1/(3*2) * (x - x_h3)**3, \
                       int((x > (x_h2-d_a/2))) * np.sind(theta) * 1/(3*2) * (x - (x_h2-d_a/2))**3, \
                      x, \
                      1])
    return avec, const

def getDispCoefficients_y(x, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta):
    const =             -q*np.sind(theta)*1/(4*3*2)*x**4 \
            - int((x > (x_h2 + d_a/2))) * P_2*np.cosd(theta)*1/(3*2)*(x - (x_h2 + d_a/2))**3 \
            - int((x > (x_h2 - d_a/2))) * P_1*np.cosd(theta)*1/(3*2)*(x - (x_h2 - d_a/2))**3
    avec  = np.array([-int((x > x_h1)) * 1/(3*2) * (x - x_h1)**3,\
                      -int((x > x_h2)) * 1/(3*2) * (x - x_h2)**3, \
                      -int((x > x_h3)) * 1/(3*2) * (x - x_h3)**3, \
                      x, \
                      1])
    return avec, const


def zBendingSolver(x_h1, x_h2, x_h3, P_2, d_a, q, theta, l_a, d_1, d_3, E, I_zz):
    # --- OUTPUTS ---
    # 
    
    # system of equations: (solution vector)
    # 
    # | F_1y | F_2y | F_3y | P_1 | c_1 | c_2 |
    
    np.cosd = lambda x : np.cos( np.deg2rad(x) )
    np.sind = lambda x : np.sin( np.deg2rad(x) )
    

    
    avec = np.zeros((6,6))
    bvec = np.zeros((6))
    
    # generate the linear equation vectors for the statics equations
    # sum of forces in y direction
    avec[0] = np.array([1,1,1,np.sind(theta), 0, 0])
    bvec[0] = q*np.cosd(theta)*l_a - np.sind(theta)*P_2
    
    # sum of moments around z
    avec[1] = np.array([x_h1,x_h2,x_h3,np.sind(theta)*(x_h2-d_a/2),0,0])
    bvec[1] = q*np.cosd(theta)*0.5*l_a**2 - np.sind(theta) * P_2*(x_h2+d_a/2)
    
    # hinge 1 condition
    avec[2],const = getDispCoefficients_z(x_h1, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    bvec[2]       = - const + d_1 * E * I_zz
    
    # hinge 2 condition
    avec[3],const = getDispCoefficients_z(x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    bvec[3]       = - const + 0 * E * I_zz
    
    # hinge 3 condition
    avec[4],const = getDispCoefficients_z(x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    bvec[4]       = - const + d_3 * E * I_zz
    
    #actuator condition
    avec[5],const = getDispCoefficients_z(x_h2-d_a/2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    bvec[5]       = - const + 0 * E * I_zz
    
    # solve the linear system
    sol = np.linalg.solve(avec, bvec)
    
    return sol


def yBendingSolver(x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta, l_a, E, I_yy):
    # --- OUTPUTS ---
    # 
    
    # system of equations: (solution vector)
    # 
    # | F_1z | F_2z | F_3z | c_1 | c_2 |
    
    np.cosd = lambda x : np.cos( np.deg2rad(x) )
    np.sind = lambda x : np.sin( np.deg2rad(x) )
    
    avec = np.zeros((5,5))
    bvec = np.zeros((5))
    
    # generate the linear equation vectors for the statics equations
    # sum of forces in y direction
    avec[0] = np.array([1,1,1, 0, 0])
    bvec[0] = - q*np.sind(theta)*l_a + np.cosd(theta)*(P_1 + P_2)
    
    # sum of moments around z
    avec[1] = np.array([-x_h1,-x_h2,-x_h3,0,0])
    bvec[1] = q*np.sind(theta) * 0.5 * l_a**2 \
              - np.cosd(theta) * P_1 * (x_h2-d_a/2) \
              - np.cosd(theta) * P_2 * (x_h2+d_a/2)
    
    # hinge 1 condition
    avec[2],const = getDispCoefficients_y(x_h1, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta)
    bvec[2]       = - const + 0 * E * I_yy
    
    # hinge 2 condition
    avec[3],const = getDispCoefficients_y(x_h2, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta)
    bvec[3]       = - const + 0 * E * I_yy
    
    # hinge 3 condition
    avec[4],const = getDispCoefficients_y(x_h3, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta)
    bvec[4]       = - const + 0 * E * I_yy
    
    # solve the linear system
    sol = np.linalg.solve(avec, bvec)
    
    return sol



def sampleBendingShape(x_vec, x_h1, x_h2, x_h3, P_2, d_a, q, theta, l_a, d_1, d_3, E, I_zz, I_yy):
    
    sol_z = zBendingSolver(x_h1, x_h2, x_h3, P_2, d_a, q, theta, l_a, d_1, d_3, E, I_zz)
    sol_y = yBendingSolver(x_h1, x_h2, x_h3, sol_z[3], P_2, d_a, q, theta, l_a, E, I_yy)
    
    d_yz_vec = np.zeros((2,len(x_vec)))
    
    i = 0
    for x in x_vec:        
        a,c = getDispCoefficients_z(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
        d_yz_vec[1,i] = (a @ sol_z + c) / E / I_zz
        
        a,c = getDispCoefficients_y(x, x_h1, x_h2, x_h3, sol_z[3], P_2, d_a, q, theta)
        d_yz_vec[0,i] = (a @ sol_y + c) / E / I_yy
        
        i = i + 1
    
    
    
    return d_yz_vec
    
    
    

def plotBendingShape(x_vec, d_yz_vec):
    
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(x_vec, d_yz_vec[0,:])
    axs[1].plot(x_vec, d_yz_vec[1,:])
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
    return 0


for k in range(4,24,4):
    test_x_vec = np.linspace(0,2770,k)
    d_yz_vec = sampleBendingShape(test_x_vec, x_h1, x_h2, x_h3, p, d_a, q, theta, l_a, d_1, d_3, E, 1e7, 5e8)
    plotBendingShape(test_x_vec, d_yz_vec)

        
    
        
        
        
    

