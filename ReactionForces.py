# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:49:59 2019

@author: tblaha
"""

from UniversalConstants import *
import numpy as np

def getDispCoefficients_y(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta):
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
    
    # constant parts of the maccaulay equation in the report, integrated 3 times
    const =            q*np.cosd(theta)*1/(4*3*2)*x**4 \
                      -int((x > (x_h2 + d_a/2))) * P_2*np.sind(theta)*1/(3*2)*(x - (x_h2 + d_a/2))**3
            
    # linear constants of the solution vector  [F_1y F_2y F_3y P_1 c_1 c_2]
    # (the a vector above)
    # this is also found by integrating 3 times and remembering to use the
    # macaulay functions
    avec  = np.array([-int((x > x_h1)) * 1/(3*2) * (x - x_h1)**3, \
                      -int((x > x_h2)) * 1/(3*2) * (x - x_h2)**3, \
                      -int((x > x_h3)) * 1/(3*2) * (x - x_h3)**3, \
                       int((x > (x_h2-d_a/2))) * np.sind(theta) * 1/(3*2) * (x - (x_h2-d_a/2))**3, \
                      x, \
                      1])
    
    return avec, const

def getDispCoefficients_z(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta):
    # Basically this assembles the "a" vector and the "const" in this equation by
    # triple integration of the internal shear force (see report). nu(x) is the
    # displacement function at the spanwise location x
    # [F_1z F_2z F_3z P_1 c_1 c_2]*a + const = nu_y(x)
    # 
    # --- INPUTS --- #
    # x          : spanwise location
    # x_hi       : hinge locations
    # P_1        : now known actuator 1 load (negative z direction, like P_2, unlike FBD)
    # P_2        : known actuator 2 load (negative z direction, like P_1, unlike FBD)
    # d_a        : distance between the actuators, centered around x_h2
    # q          : distributed load (N/mm)
    # theta      : upwards deflection of the aileron
    # 
    # --- OUTPUTS --- #
    # avec       : the a vector in the equation above
    # const      : the const vector in the equation above
    
    # same method as getDispCoefficients_z
    const =           -q*np.sind(theta)*1/(4*3*2)*x**4 \
                      -int((x > (x_h2 + d_a/2))) * P_2*np.cosd(theta)*1/(3*2)*(x - (x_h2 + d_a/2))**3
    avec  = np.array([-int((x > x_h1)) * 1/(3*2) * (x - x_h1)**3, \
                      -int((x > x_h2)) * 1/(3*2) * (x - x_h2)**3, \
                      -int((x > x_h3)) * 1/(3*2) * (x - x_h3)**3, \
                      -int((x > (x_h2-d_a/2))) * np.cosd(theta) * 1/(3*2) * (x - (x_h2-d_a/2))**3, \
                      x, \
                      1])
    
    return avec, const


def BendingSolver(x_h1, x_h2, x_h3, P_2, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_zz, I_yy):
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
    bvec = np.zeros((dim))
    
    
    
    # ----- assembling the system ----- #
    
    # generate the linear equation vectors for the statics equations
    
    # First statics (Forces in x)
    a_mat[0,-1] = 1
    bvec[0]  = 0
    
    # Second statics (Forces in y)
    a_mat[1,0:3] = np.array([1, 1, 1])
    a_mat[1,3]   = np.array([np.sind(theta)])
    bvec[1]      = - ( P_2*np.sind(theta) - q*l_a*np.cosd(theta) )
    
    # Third statics (Forces in z)
    a_mat[2,6:9] = np.array([1, 1, 1])
    a_mat[2,3]   = np.array([-np.cos(theta)])
    bvec[2]      = - ( - P_2*np.cos(theta) + q*l_a*np.sind(theta))
    
    # Forth statics (Moments around x)
    st_4 = np.zeros((dim))
    st_4[6:9] = np.array([d_1, 0, d_3])
    st_4[3]   = np.array([-h_a * np.sqrt(2)/2 * np.cosd(theta+45)])
    st_4_b    = - ( -q*np.cos(theta)*(c_a/4 - h_a/2) - P_2 * h_a * np.sqrt(2)/2 * np.cosd(theta+45) )
    
    # Fifth statics (Moments around y)
    a_mat[4,6:9] = np.array([-x_h1, -x_h2, -x_h3])
    a_mat[4,3]   = np.array([np.cosd(theta)*(x_h2 - d_a/2)])
    bvec[4]      = - (P_2 * np.cosd(theta)*(x_h2 + d_a/2) - q*np.sind(theta)*l_a**2/2)
    
    # sixth statics (Moment around z)
    a_mat[5,0:3] = np.array([x_h1, x_h2, x_h3])
    a_mat[5,3]   = np.array([-np.sind(theta)*(x_h2 - d_a/2)])
    bvec[5]      = - (- P_2 * np.sind(theta)*(x_h2 + d_a/2) - q*np.cosd(theta)*l_a**2/2)
    
#    # sum of forces in y direction
#    a_mat[0] = np.array([1,1,1,np.sind(theta), 0, 0])
#    bvec[0] = q*np.cosd(theta)*l_a - np.sind(theta)*P_2
#    
#    # sum of moments around z
#    a_mat[1] = np.array([x_h1,x_h2,x_h3,np.sind(theta)*(x_h2-d_a/2),0,0])
#    bvec[1] = q*np.cosd(theta)*0.5*l_a**2 - np.sind(theta) * P_2*(x_h2+d_a/2)
    
    # hinge 1 y-condition
    a_temp,const = getDispCoefficients_y(x_h1, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[6,0:6] = a_temp
    bvec[6]      = - const + d_1 * np.cosd(theta) * E * I_zz
    
    # hinge 2 y-condition
    a_temp,const = getDispCoefficients_y(x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[7,0:6] = a_temp
    bvec[7]      = - const + 0   * np.cosd(theta) * E * I_zz
    
    # hinge 3 y-condition
    a_temp,const = getDispCoefficients_y(x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[8,0:6] = a_temp
    bvec[8]      = - const + d_3 * np.cosd(theta) * E * I_zz
    
    # hinge 1 z-condition
    a_temp,const   = getDispCoefficients_z(x_h1, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[9,6:9]   = a_temp[0:3]
    a_mat[9,9:11]  = a_temp[4:]
    a_mat[9,3]     = a_temp[3]
    bvec[9]        = - const + d_1 * np.sind(theta) * E * I_yy
    
    # hinge 2 z-condition
    a_temp,const   = getDispCoefficients_z(x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[10,6:9]  = a_temp[0:3]
    a_mat[10,9:11] = a_temp[4:]
    a_mat[10,3]    = a_temp[3]
    bvec[10]       = - const + 0   * np.sind(theta) * E * I_yy
    
    # hinge 3 z-condition
    a_temp,const   = getDispCoefficients_z(x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[11,6:9]  = a_temp[0:3]
    a_mat[11,9:11] = a_temp[4:]
    a_mat[11,3]    = a_temp[3]
    bvec[11]       = - const + d_3 * np.sind(theta) * E * I_yy
#    
#    # hinge 2 y-condition
#    a_temp,const = getDispCoefficients_z(x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
#    a_mat[7,0:6] = a_temp
#    bvec[7]      = - const + 0   * E * I_zz
#    
#    # hinge 3 y-condition
#    a_temp,const = getDispCoefficients_z(x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
#    a_mat[8,0:6] = a_temp
#    bvec[8]      = - const + d_3 * E * I_zz
#    
#    
#    # hinge 2 condition
#    a_mat[3],const = getDispCoefficients_z(x_h2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
#    bvec[3]       = - const + 0 * E * I_zz
#    
#    # hinge 3 condition
#    a_mat[4],const = getDispCoefficients_z(x_h3, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
#    bvec[4]       = - const + d_3 * E * I_zz
#    
#    #actuator condition
#    a_mat[5],const = getDispCoefficients_z(x_h2-d_a/2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
#    bvec[5]       = - const + 0 * E * I_zz
    
    
    # [F_1y F_2y F_3y P_1 c_1y c_2y F_1z F_2z F_3z c_1z c_2z F_2x]
    #
    # Actuator compatibility
    a_temp,const = getDispCoefficients_y(x_h2-d_a/2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[3,0:6] = np.sind(theta)/np.cosd(theta)*a_temp[0:6] / I_zz
    bvec[3]      = - ( np.sind(theta)/np.cosd(theta)*const / I_zz)
    a_temp,const = getDispCoefficients_z(x_h2-d_a/2, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
    a_mat[3,6:9] = a_temp[0:3]/ I_yy
    a_mat[3,3]  += a_temp[3]/ I_yy
    a_mat[3,9:11] = a_temp[4:]/ I_yy
    bvec[3]     += - (const / I_yy)
    
    # or: last statics eq
    #a_mat[3,:] = st_4
    #bvec[3]    = st_4_b
    
    # solve the linear system
    sol = np.linalg.solve(a_mat, bvec)
    
    
    
    # assert statics
    diff = st_4 @ sol - st_4_b
    
    
    
    return sol


def yBendingSolver(x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta, l_a, E, I_yy):
    # --- OUTPUTS ---
    # 
    
    # system of equations: (solution vector)
    # 
    # | F_1z | F_2z | F_3z | c_1 | c_2 |
    
    np.cosd = lambda x : np.cos( np.deg2rad(x) )
    np.sind = lambda x : np.sin( np.deg2rad(x) )
    
    a_mat = np.zeros((5,5))
    bvec = np.zeros((5))
    
    # generate the linear equation vectors for the statics equations
    # sum of forces in y direction
    a_mat[0] = np.array([1,1,1, 0, 0])
    bvec[0] = - q*np.sind(theta)*l_a + np.cosd(theta)*(P_1 + P_2)
    
    # sum of moments around z
    a_mat[1] = np.array([-x_h1,-x_h2,-x_h3,0,0])
    bvec[1] = q*np.sind(theta) * 0.5 * l_a**2 \
              - np.cosd(theta) * P_1 * (x_h2-d_a/2) \
              - np.cosd(theta) * P_2 * (x_h2+d_a/2)
    
    # hinge 1 condition
    a_mat[2],const = getDispCoefficients_y(x_h1, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta)
    bvec[2]       = - const + 0 * E * I_yy
    
    # hinge 2 condition
    a_mat[3],const = getDispCoefficients_y(x_h2, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta)
    bvec[3]       = - const + 0 * E * I_yy
    
    # hinge 3 condition
    a_mat[4],const = getDispCoefficients_y(x_h3, x_h1, x_h2, x_h3, P_1, P_2, d_a, q, theta)
    bvec[4]       = - const + 0 * E * I_yy
    
    # solve the linear system
    sol = np.linalg.solve(a_mat, bvec)
    
    return sol



def sampleBendingShape(x_vec, x_h1, x_h2, x_h3, P_2, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_zz, I_yy):
    
    sol = BendingSolver(x_h1, x_h2, x_h3, P_2, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, I_zz, I_yy)
    sol_y = sol[0:6]
    
    sol_z = np.zeros(6)
    sol_z[0:3] = sol[6:9]
    sol_z[3]   = sol[3]
    sol_z[4:]  = sol[9:11]
    
    d_yz_vec = np.zeros((2,len(x_vec)))
    
    i = 0
    for x in x_vec:        
        a,c = getDispCoefficients_z(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
        d_yz_vec[1,i] = (a @ sol_z + c) / E / I_yy
        
        a,c = getDispCoefficients_y(x, x_h1, x_h2, x_h3, P_2, d_a, q, theta)
        d_yz_vec[0,i] = (a @ sol_y + c) / E / I_zz
        
        i = i + 1
    
    
    
    return d_yz_vec, sol[-1], sol_y[0:3], sol_z[0:3], sol[3]
    
    
    

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


#for k in range(32,36,4):
#    test_x_vec = np.linspace(0,2770,k)
#    d_yz_vec, Fx, Fy, Fz, P = sampleBendingShape(test_x_vec, x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, 1e7, 5e8)
#    plotBendingShape(test_x_vec, d_yz_vec)

        
d, Fx, Fy, Fz, P1 = sampleBendingShape([0, 153, 1281-280/2, 1281, 2681, 2771], x_h1, x_h2, x_h3, p, d_a, q, theta, c_a, h_a, l_a, d_1, d_3, E, 1e7, 5e8)

#print(np.arctan(d[1,2] / d[0,2]) * 180/np.pi)
        
    

