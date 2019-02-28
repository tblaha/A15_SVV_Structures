# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:49:59 2019

@author: tblaha
"""

from UniversalConstants import *
import numpy as np
from RotateReactions import *


# solution vector [  0   1   2    3    4    5    6    7   8   9   10  11]
# solution vector [F_1y F_2y F_3y F_1z F_2z F_3z F_2x c_1 c_2 c_3 c_4 P_1];

def getBendingTerms(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta, E, I_yy, I_zz):
    # takes aileron dimensions and a spanwise location to compute coefficients
    # that will later be used to solve the macaulay functions and while sampling 
    # the displacements
    #
    # Basically this assembles the "a" vector and the "const" in this equation by
    # triple integration of the internal shear force (see report). nu(x) is the
    # displacement function:
    # [F_1y F_2y F_3y P_1 c_1 c_2]*a + const = nu_z(x)
    #
    # --- INPUTS --- #
    # x          : spanwise location
    # x_hi       : hinge locations
    # P_2        : known actuator 2 load (negative z direction, like P_1, unlike FBD)
    # d_a        : distance between the actuators, centered around x_h2
    # q          : distributed load (N/mm)
    # theta      : upwards deflection of the aileron
    #
    # --- OUTPUTS --- #
    # avec       : the a vector in the equation above
    # const      : the const vector in the equation above
    
    
    ay     = np.zeros((12,1))
    ay[0]  = max(0, (x-x_h1))**3 * 1 / (E*I_zz*3*2) # F_1y
    ay[1]  = max(0, (x-x_h2))**3 * 1 / (E*I_zz*3*2) # F_2y
    ay[2]  = max(0, (x-x_h3))**3 * 1 / (E*I_zz*3*2) # F_3y
    ay[7]  = x
    ay[11] = max(0, (x-(x_h2 - d_a/2)))**3 * 1 / (E*I_zz*3*2) * (-np.sind(theta)) # P_1
    
    cy     = q*(-x**4/(4*3*2 * E*I_zz) * np.cosd(theta))\
             + P_2 * max(0, (x-(x_h2 + d_a/2)))**3 * 1 / (E*I_zz*3*2) * (-np.sind(theta)) # P_2
    
    az     = np.zeros((12,1))
    az[3]  = max(0, (x-x_h1))**3 * 1 / (E*I_yy*3*2) # F_1y
    az[4]  = max(0, (x-x_h2))**3 * 1 / (E*I_yy*3*2) # F_2y
    az[5]  = max(0, (x-x_h3))**3 * 1 / (E*I_yy*3*2) # F_3y
    az[9]  = x
    az[11] = max(0, (x-(x_h2 - d_a/2)))**3 * 1 / (E*I_yy*3*2) * (-np.cosd(theta)) # P_1
    
    cz     = q*(x**4/(4*3*2 * E*I_yy) * np.sind(theta))\
             + P_2 * max(0, (x-(x_h2 + d_a/2)))**3 * 1 / (E*I_yy*3*2) * (-np.cosd(theta)) # P_2
    
    
    return ay, cy, az, cz



# solution vector [  0   1   2    3    4    5    6    7   8   9   10  11]
# solution vector [F_1y F_2y F_3y F_1z F_2z F_3z F_2x c_1 c_2 c_3 c_4 P_1];

def getShearTerms(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta, k, A, G):
    # takes aileron dimensions and a spanwise location to compute coefficients
    # that will later be used to solve the macaulay functions and while sampling 
    # the displacements
    #
    # Basically this assembles the "a" vector and the "const" in this equation by
    # triple integration of the internal shear force (see report). nu(x) is the
    # displacement function:
    # [F_1y F_2y F_3y P_1 c_1 c_2]*a + const = nu_z(x)
    #
    # --- INPUTS --- #
    # x          : spanwise location
    # x_hi       : hinge locations
    # P_2        : known actuator 2 load (negative z direction, like P_1, unlike FBD)
    # d_a        : distance between the actuators, centered around x_h2
    # q          : distributed load (N/mm)
    # theta      : upwards deflection of the aileron
    #
    # --- OUTPUTS --- #
    # avec       : the a vector in the equation above
    # const      : the const vector in the equation above
    
    
    ay     = np.zeros((12,1))
    ay[0]  = max(0, (x-x_h1))**1 * -1 / (k*A*G) # F_1y
    ay[1]  = max(0, (x-x_h2))**1 * -1 / (k*A*G) # F_2y
    ay[2]  = max(0, (x-x_h3))**1 * -1 / (k*A*G) # F_3y
    ay[11] = max(0, (x-(x_h2 - d_a/2)))**1 * 1 / (k*A*G) * (np.sind(theta)) # P_1
    
    cy     = q*(x**2/(2 * k*A*G) * np.cosd(theta))\
             + P_2 * max(0, (x-(x_h2 + d_a/2)))**1 * 1 / (k*A*G) * (np.sind(theta)) # P_2
    
    az     = np.zeros((12,1))
    az[3]  = max(0, (x-x_h1))**1 * 1 / (k*A*G) # F_1y
    az[4]  = max(0, (x-x_h2))**1 * 1 / (k*A*G) # F_2y
    az[5]  = max(0, (x-x_h3))**1 * 1 / (k*A*G) # F_3y
    az[11] = max(0, (x-(x_h2 - d_a/2)))**1 * 1 / (k*A*G) * (np.cosd(theta)) # P_1
    
    cz     = -q*(x**2/(2 * k*A*G) * np.sind(theta))\
             + P_2 * max(0, (x-(x_h2 + d_a/2)))**1 * 1 / (k*A*G) * (np.cosd(theta)) # P_2
    
    
    return ay, cy, az, cz



def BendingSolver(x_h1, x_h2, x_h3, P_2, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_yy, I_zz, k, A, G):
    # does the heavy lifting of computing reaction forces, actuator 1 force
    # and getting all the info needed for computing the shape
    #
    # --- INPUTS --- #
    # x_hi       : hinge locations
    # P_2        : known actuator 2 load (negative z direction, like P_1, unlike FBD)
    # d_a        : distance between the actuators, centered around x_h2
    # q          : distributed load (N/mm)
    # theta      : upwards deflection of the aileron
    # l_a        : length of the aileron
    # d_1, d_3   : known displacements at hinge 1 and 3
    # E          : youngs modulus of the material
    # I_zz       : moment of inertia
    #
    # --- OUTPUTS --- #
    # sol        : [F_1y F_2y F_3y P_1 c_1y c_2y F_1z F_2z F_3z c_1z c_2z F_2x]; the solution vector to the
    #              linear system
    #
    
    # ----- strategy ----- #
    # Assembling each equation of the system line-by-line. Then solving the 
    # non-singular matrix equation.
    # There will be six equations (4 from displacement compatibility and 2
    # from the statics of the system)
    
    
    
    # ----- not so interesting ----- #
    # helper functions to make the code prettier (cos and sin for deg, not rad)
    np.cosd = lambda x : np.cos( np.deg2rad(x) )
    np.sind = lambda x : np.sin( np.deg2rad(x) )
    
    # preallocate a matrix and b vector
    dim = 12
    a_mat = np.zeros((dim,dim))
    b_vec = np.zeros((dim))
    
    
    
    # ----- assembling the system ----- #
    
    # generate the linear equation vectors for the statics equations
    
    # First statics (Forces in x)
    a_mat[0,6] = 1
    b_vec[0]     = 0
    
    # Second statics (Forces in y)
    a_mat[1,0:3] = np.array([1, 1, 1])
    a_mat[1,-1]   = np.array([-np.sind(theta)])
    b_vec[1]     = - ( - P_2*np.sind(theta) - q*l_a*np.cosd(theta) )
    
    # Third statics (Forces in z)
    a_mat[2,3:6] = np.array([1, 1, 1])
    a_mat[2,-1]   = np.array([-np.cosd(theta)])
    b_vec[2]     = - ( - P_2*np.cosd(theta) + q*l_a*np.sind(theta))
    
    # Forth statics (Moments around x)
    #a_mat[3,3:6] = np.array([d_1*np.cosd(theta), 0, d_3*np.cosd(theta)])
    a_mat[3,3:6] = np.array([0, 0, 0])
    a_mat[3,-1]   = np.array([-h_a * np.sqrt(2)/2 * np.cosd(theta+45)]) #proper line
    #a_mat[3,-1]   = np.array([-h_a / 2 * np.cosd(theta)]) This line works more like the verification model
    b_vec[3]     = - ( -q * l_a * np.cosd(theta)*(c_a/4 - h_a/2) - P_2 * h_a * np.sqrt(2)/2 * np.cosd(theta+45)) #proper line
    #b_vec[3]     = - ( -q * l_a * np.cosd(theta)*(c_a/4 - h_a/2) - P_2 * h_a /2 * np.cosd(theta) ) #This line works more like the verification model
    
    # Fifth statics (Moments around y)
    a_mat[4,3:6] = np.array([-x_h1, -x_h2, -x_h3])
    a_mat[4,-1]   = np.array([np.cosd(theta)*(x_h2 - d_a/2)])
    b_vec[4]     = - (P_2 * np.cosd(theta)*(x_h2 + d_a/2) - q*np.sind(theta)*l_a**2/2)
    
    # sixth statics (Moment around z)
    a_mat[5,0:3] = np.array([x_h1, x_h2, x_h3])
    a_mat[5,-1]   = np.array([-np.sind(theta)*(x_h2 - d_a/2)])
    b_vec[5]     = - (- P_2 * np.sind(theta)*(x_h2 + d_a/2) - q*np.cosd(theta)*l_a**2/2)
    
#    # sum of forces in y direction
#    a_mat[0] = np.array([1,1,1,np.sind(theta), 0, 0])
#    bvec[0] = q*np.cosd(theta)*l_a - np.sind(theta)*P_2
#    
#    # sum of moments around z
#    a_mat[1] = np.array([x_h1,x_h2,x_h3,np.sind(theta)*(x_h2-d_a/2),0,0])
#    bvec[1] = q*np.cosd(theta)*0.5*l_a**2 - np.sind(theta) * P_2*(x_h2+d_a/2)
    
    # hinge 1 conditions
    ayb,cyb,azb,czb  = getBendingTerms(x_h1, x_h1, x_h2, x_h3, P_2, d_a, q, theta, E, I_yy, I_zz)
    ays,cys,azs,czs  = getShearTerms  (x_h1, x_h1, x_h2, x_h3, P_2, d_a, q, theta, k, A, G)
    
    a_mat[6] = np.transpose(ayb + ays)
    a_mat[7] = np.transpose(azb + azs)
    #a_mat[7] = np.transpose(azb)
    
    # integration constants
    a_mat[6,8]  = 1
    a_mat[7,10] = 1
    
    b_vec[6] = - (cyb + cys) + d_1 * np.cosd(theta)
    b_vec[7] = - (czb + czs) - d_1 * np.sind(theta)
    #b_vec[7] = - (czb) - d_1 * np.sind(theta)
    
    
    
    # hinge 2 conditions
    ayb,cyb,azb,czb  = getBendingTerms(x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta, E, I_yy, I_zz)
    ays,cys,azs,czs  = getShearTerms  (x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta, k, A, G)
    
    a_mat[8] = np.transpose(ayb + ays)
    a_mat[9] = np.transpose(azb + azs)
    #a_mat[9] = np.transpose(azb)
    
    # integration constants
    a_mat[8,8]  = 1
    a_mat[9,10] = 1
    
    b_vec[8] = - (cyb + cys) + 0 * np.cosd(theta)
    b_vec[9] = - (czb + czs) + 0 * np.sind(theta)
    #b_vec[9] = - (czb) + 0 * np.sind(theta)
    
    
    
    # hinge 3 conditions
    ayb,cyb,azb,czb  = getBendingTerms(x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta, E, I_yy, I_zz)
    ays,cys,azs,czs  = getShearTerms  (x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta, k, A, G)
    
    a_mat[10] = np.transpose(ayb + ays)
    a_mat[11] = np.transpose(azb + azs)
    
    # integration constants
    a_mat[10,8]  = 1
    a_mat[11,10] = 1
    
    b_vec[10] = - (cyb + cys) + d_3 * np.cosd(theta)
    b_vec[11] = - (czb + czs) - d_3 * np.sind(theta)
    #b_vec[11] = - (czb) - d_3 * np.sind(theta)
    
    
       
    # solve the linear system
    sol = np.linalg.solve(a_mat, b_vec)
    
    
    
    # assert statics
    diff = a_mat[3] @ sol - b_vec[3]
    
    
    return sol



def sampleBendingShape(x_vec, x_h1, x_h2, x_h3, P_2, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_yy, I_zz, k, A, G):
    
    sol = BendingSolver(x_h1, x_h2, x_h3, P_2, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_yy, I_zz, k, A, G)
       
    d_yz_vec = np.zeros((2,len(x_vec)))
    
    i = 0
    for x in x_vec:        
        ayb,cyb,azb,czb = getBendingTerms(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta, E, I_yy, I_zz)
        ays,cys,azs,czs = getShearTerms  (x, x_h1, x_h2, x_h3, P_2, d_a, q, theta, k, A, G)
        
        
        
        d_yz_vec[0,i] = sol @ (ayb + ays + np.array([[0],[0],[0],[0],[0],[0],[0],[0],[1],[0],[0],[0]])) + cyb + cys
        d_yz_vec[1,i] = sol @ (azb + azs + np.array([[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[0]])) + czb + czs
        
        i = i + 1
    
    
    return d_yz_vec, sol[6], sol[0:3], sol[3:6], -sol[-1]
    
    
    

def plotBendingShape(x_vec, d_yz_vec):
    # plots the shapes generated by the deflections, both in 2D
    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(x_vec, d_yz_vec[0,:])
    axs[1].plot(x_vec, d_yz_vec[1,:])
    
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
    return 0


    

