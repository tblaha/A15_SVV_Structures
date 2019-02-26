# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:59:15 2019

@author: Till
"""

import numpy as np

def generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, cg_correction):
    # Takes the geometry, the number of stiffeners and the number of booms in
    # between each 2 stiffeners and computes boom locations and corresponding 
    # areas
    #
    # --- INPUTS --- #
    # h_a                 : height of aileron [mm] (float)
    # c_a                 : chord length of aileron [mm] (float)
    # n_st                : The amount of equally spaced stiffeners along the
    #                       perimiter of the skin panels [-] (int)
    # A_st                : Stiffener area [mm^2] (float) = (w_st+h_st-t_st)*t_st
    # t_sk                : skin thickness [mm] (float)
    # t_sp                : spar thickness [mm] (float)
    #
    # --- OUTPUTS --- #
    # 2d numpy array:
    # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # y and z locations are from the hinge-line of the section
    # cell id: 1 (exclusively left cell, counter clockwise sorted)
    #          2 (exclusively right cell, counter clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    
    
    # ----- preallocation ----- #
    # in total there will be n_st stiffeners, so prealloc that
    S = np.zeros((n_st, 4))
    
    
    
    # ----- Length and numbers of booms ----- #
    # compute the lenth of the in-between segments and 
    # calculate the amount of stiffeners and booms (stiffeners <= booms) in the
    # circular section
    
    # Find total arc length of the semi circle
    sc_arc_length = h_a*np.pi/2
    
    # Total length of the straight sections
    straight_length = 2*np.sqrt((h_a/2)**2 + (c_a-h_a/2)**2)
    
    # Total length
    total_length = sc_arc_length + straight_length
    
    # length per segment in between stiffeners
    length_per_stiff_seg = total_length/(len(S))
    
    # number of stiffeners and booms in the circular segment
    stiffs_quarter_circular = np.floor(sc_arc_length/2/length_per_stiff_seg)
    
    
    # ----- booms in circular section ----- #
    # iterate over the amount of booms (CCW) in the circular section (using the
    # angle that the lines connecting the hinge line and the booms make) and
    # compute their area by taking skin contributions and adding the stiffener
    # area where there is a stiffener
    
    # iterate over the booms in the circular section
    for i in range(int(stiffs_quarter_circular)*2+1): # +1 because there is one on the z-axis
        
        # the radial distance of each boom in the circular section is constant,
        # so only the angle needs to be calculated: 0 angle means on the z-axis
        # and positive angle means below the z-axis
        angle = (stiffs_quarter_circular - i) * length_per_stiff_seg/(2*sc_arc_length) * 2*np.pi
        
        # stiffener angle
        S[i,3]     = -np.pi/2 - angle
        
        # using the angle, get the location using the radial distance h_a/2
        S[i,0]     = np.sin(angle)*h_a/2
        S[i,1]     = np.cos(angle)*h_a/2
        
        # centroid location
        u_vec = np.array([np.cos(S[i,3]), np.sin(S[i,3])])
        if cg_correction:
            S[i,0:2]  = S[i,0:2] + u_vec * Ybar_st
            
        
        # all the stiffeners computed in this for-loop are in beam section 1
        S[i,2]     = 1
        
        # corrected stiffener area
        

        

    
    
    # ----- booms in straight sections ----- #
    # compute the boom locations and areas in the same general way as above 
    # but now for the bottom straight segement. Then, basically reverse the
    # and mirror the locations to the top straight segment.
    
    # compute the length in the straight segment for when the first boom
    # appears (straight_sec_start)
    leftover_arc_length = sc_arc_length/2 - angle*h_a/2 # arc length still in circular segment
    straight_sec_start  = length_per_stiff_seg-leftover_arc_length%length_per_stiff_seg
        
    # stiffeners and booms in either of the two straight segments
    stiffs_half_straight    = np.floor((straight_length/2-straight_sec_start)/length_per_stiff_seg)
        
    # iterate again
    for j in range(int(stiffs_half_straight)+1):
        
        # count up i (i will be used as the index in B throughout)
        i = i + 1
        
        # direction vector that the booms will be on (representing the straight
        # line from [0,-h_a/2] to [h_a/2-c_a, 0])
        unit_vec = np.array([[h_a/2], [-c_a+h_a/2]])
        unit_vec = unit_vec/np.linalg.norm(unit_vec)
        
        # starting point of that line
        bottom_pnt = np.array([[-h_a/2],[0]])
        
        # multiply the arc length from the starting point to the boom i (which
        # is (straight_sec_start + j * length_per_boom_seg)) to the unit_vec
        # and add the result to the bottom point
        S[i,0:2]   = np.transpose(bottom_pnt + unit_vec * (straight_sec_start + j * length_per_stiff_seg))
        
        # angle
        S[i,3]     = np.arctan2(h_a/2 , c_a-h_a/2)
        
        # actual location
        u_vec = np.array([np.cos(S[i,3]), np.sin(S[i,3])])
        if cg_correction:
            S[i,0:2]   = S[i,0:2] + u_vec * Ybar_st
        
        # we are in section 2
        S[i,2]     = 2
        
        
        
    # second (top) straight segment by mirroring the booms
    k = i # index in the B array to call the booms computed for the bottom
    for j in range(int(stiffs_half_straight)+1):
        i = i + 1
        
        # mirroring about the z-axis
        S[i,0:2] = S[k, 0:2] * np.array([[-1, 1]])
        
        # angle
        S[i,3]   = np.arctan2(h_a/2 , -c_a+h_a/2)
        
        # still section 2
        S[i,2]   = 2
        
        # count down the index to move to the next boom of the bottom
        k = k - 1
        
    # finally, return the booms
    return  S

#plotCrossSection(generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 1), generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 0))

