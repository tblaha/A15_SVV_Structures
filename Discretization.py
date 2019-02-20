# -*- coding: utf-8 -*-
"""
Author: tblaha & dverkooij
Date  : 2019-02-18
"""

from UniversalConstants import *
import numpy as np

import matplotlib.pyplot as plt

def discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_c, z_c, booms_between):
    # Takes the geometry, the number of stiffeners and the number of booms in
    # between each stiffener and compute boom locations and areas
    #
    # --- INPUTS --- #
    # h_a                 : height of aileron (float)
    # c_a                 : chord length of aileron (float)
    # n_st                : The amount of equally spaced stiffeners along the
    #                       perimiter of the skin panels (int)
    # A_st                : Stiffener area
    # t_sk                : skin thickness
    # t_sp                : spar thickness
    # booms_between       : The amount of booms in between stiffeners; 
    #                       stiffeners themselves are automatically booms (int)
    # --- OUTPUTS --- #
    # 2d numpy array:
    # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # cell id: 1 (exclusively left cell, counter clockwise sorted)
    #          2 (exclusively right cell, counter clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    
    spar_upscaling = 4
    
    # we know that there are n_st+booms_between*(n_st+1) booms, so we can
    # iterate over that range and figure out each boom
    S = np.zeros((n_st+1, 5))
    B = np.zeros((n_st+booms_between*(n_st+1+spar_upscaling)+2, 5))
    
    # Find total arc length of the semi circle
    sc_arc_length = h_a*np.pi/2
    
    # Total length of the 2 straight sections
    straight_length = 2*np.sqrt((h_a/2)**2 + (c_a-h_a/2)**2)
    
    # Total length
    total_length = sc_arc_length + straight_length
    
    # length per segment
    length_per_stiff_seg = total_length/(len(S))
    length_per_boom_seg  = total_length/(len(B)-booms_between*spar_upscaling-2)
    
    # stiffeners in the circular segment
    stiffs_quarter_circular = np.floor(sc_arc_length/2/length_per_stiff_seg)
    booms_quarter_circular  = np.floor(sc_arc_length/2/length_per_boom_seg)
    
    # going counter clockwise from the first boom in the circular sections,
    # where is the first stiffener?
    booms_to_first_stiff = (booms_quarter_circular)%(booms_between+1)
    
    # booms in circular section
    for i in range(int(booms_quarter_circular)*2+1):
        unit_angle = (booms_quarter_circular - i) * length_per_boom_seg/(2*sc_arc_length) * 2*np.pi
        B[i,0]     = np.sin(unit_angle)*h_a/2
        B[i,1]     = np.cos(unit_angle)*h_a/2
        B[i,4]     = 1
        if i:
            if abs(B[i,1]-z_c) > 1e-6:
                B[i,2]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            if abs(B[i-1,1]-z_c) > 1e-6:
                B[i-1,2] += t_sk/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            if abs(B[i,0]-y_c) > 1e-6:
                B[i,3]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            if abs(B[i-1,0]-y_c) > 1e-6:
                B[i-1,3] += t_sk/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        # Add stiffener area
        if not (i-booms_to_first_stiff)%(booms_between+1):
            B[i,2]   += A_st
            B[i,3]   += A_st
        
        # Fix corner cases
        if i == 0:
            B[i,2]  += t_sk/6 * (np.pi/2 - unit_angle) * h_a/2 * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * (np.pi/2 - unit_angle) * h_a/2 * (2 + (h_a/2-y_c)/(B[i,0]-y_c))
            
        if i == int(booms_quarter_circular)*2+1-1:
            B[i,2]  += t_sk/6 * (np.pi/2 + unit_angle) * h_a/2 * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * (np.pi/2 + unit_angle) * h_a/2 * (2 + (-h_a/2-y_c)/(B[i,0]-y_c))
            
            
    leftover_arc_length = sc_arc_length/2 - unit_angle*h_a/2
    straight_sec_start  = length_per_boom_seg-leftover_arc_length%length_per_boom_seg
    
    # stiffeners in the straight segment
    stiffs_half_straight    = np.floor((straight_length/2-straight_sec_start)/length_per_stiff_seg)
    booms_half_straight     = np.floor((straight_length/2-straight_sec_start)/length_per_boom_seg)
        
    # booms in straight section
    for j in range(int(booms_half_straight)):
        i = i + 1
        
        unit_vec = np.array([[h_a/2], [-c_a+h_a/2]])
        unit_vec = unit_vec/np.linalg.norm(unit_vec)
        
        bottom_pnt = np.array([[-h_a/2],[0]])
        
        B[i,0:2]   = np.transpose(bottom_pnt + unit_vec * (straight_sec_start + j * length_per_boom_seg))
        B[i,4]     = 2
        
        if j:
            B[i,2]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            B[i-1,2] += t_sk/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            B[i,3]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            B[i-1,3] += t_sk/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        if not (i-booms_to_first_stiff)%(booms_between+1):
            B[i,2]   += A_st
            B[i,3]   += A_st
    
        # Fix corner cases
        if j == 0:
            B[i,2]  += t_sk/6 * straight_sec_start * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * straight_sec_start * (2 + (-h_a/2-y_c)/(B[i,0]-y_c))
            
    
    k = i
    
    for j in range(int(booms_half_straight)):
        i = i + 1
        
        B[i,0:2] = B[k, 0:2] * np.array([[-1, 1]])
        B[i,4]   = 2
        
        k = k - 1
        
        if j:
            B[i,2]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            B[i-1,2] += t_sk/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            B[i,3]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            B[i-1,3] += t_sk/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        if not (i-booms_to_first_stiff-booms_between+2)%(booms_between+1):
            B[i,2]   += A_st
            B[i,3]   += A_st
            
        # Fix corner cases            
        if j == int(booms_half_straight)-1:
            B[i,2]  += t_sk/6 * straight_sec_start * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * straight_sec_start * (2 + (h_a/2-y_c)/(B[i,0]-y_c))
        
    # booms in spar section
    for l in range(booms_between*spar_upscaling+2):
        i = i + 1
        
        B[i, 0:2] = np.array([ -l * h_a / (booms_between*spar_upscaling+1) + h_a/2, 0] )
        B[i,4]    = 3
        
        if l:
            B[i,2]   += t_sp/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            B[i-1,2] += t_sp/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            B[i,3]   += t_sp/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            B[i-1,3] += t_sp/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        if l == 0:
            B[i,2]   += t_sp/6 * length_per_boom_seg * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]   += t_sp/6 * length_per_boom_seg * (2 + (h_a/2-y_c)/(B[i,0]-y_c))
            
        if l == booms_between*spar_upscaling+2-1:
            B[i,2]   += t_sp/6 * length_per_boom_seg * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]   += t_sp/6 * length_per_boom_seg * (2 + (-h_a/2-y_c)/(B[i,0]-y_c))
        
    return  B
       

 
def plotCrossSection(h_a, c_a, n_st, B):

    import matplotlib.pyplot as plt
    fig, axs = plt.subplots(2, 1)
    axs[0].scatter(B[:,1], B[:,0], B[:,2])
    axs[1].scatter(B[:,1], B[:,0], B[:,3])
    
    axs[0].axis('equal')
    axs[1].axis('equal')
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    fig.tight_layout()
    plt.show()
    
    
for i in range(10,-1,-1):
    B = discretizeCrossSection(h_a, c_a, n_st, t_st*(w_st+h_st-t_st), t_sk, t_sp, 0, -98, i)
    plotCrossSection(h_a, c_a, n_st, B)
    
    
def discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, nodes_between=50,ec=0.0001,offset=30):
    # Takes the spanwise characteristics of the aileron and computes a
    # discretization at which the deflection of leading edge and trailing edge
    # will be computed later. Spanwise nodes (the x-location of the discrete
    # cross sections) are closer to spanwise items like ribs and actuators,
    # since a lot of the stresses
    #
    # --- INPUTS --- #
    # x_h1, x_h2, x_h3    : locations of the hinges
    # d_a                 : distance between the actuators; centred in hinge 2
    # l_a                 : overall length of the aileron
    # nodes_between       : needs to be a positive, even number! The spanwise
    #                       nodes in between two spanwise "events"
    #                       (rib, hinge and one of the two ends)
    # ec                  : ec, edge_correction, makes sure no points land on
    #                       any points that have discontinuties
    # offset              : The points are distributed according to a logarithm
    #                       this logarithm can be the start of a base 10 log,
    #                       or it can be somewhat further, decreasing the
    #                       concentration of points near the edge.
    # --- OUTPUTS --- #
    # 1d numpy array: of the x-locations (NOT equally spaced)
    # | x-loc |
    # | 0     |
    # | 15.5  |
    # | ...   |
    #
    # Concentrations of nodes will exist aruond x_h1, x_h2, x_h3, x_h2+/-d_a
    
    
    #Nodes_between needs to be divisable by two to get nodes per part
    if nodes_between%2!=0:
        return "Nodes_between not divisable by two"
    nodes_between=int(nodes_between)
    nodes_per_part=int(nodes_between/2)
        
    #Also need to find the centre points of each segment
    location_list=[0,x_h1,x_h2-d_a,x_h2,x_h2+d_a,l_a]
    location_list_new=[]
    for i in range(len(location_list)-1):
        a=location_list[i]
        b=location_list[i+1]
        location_list_new.append(a)
        location_list_new.append(a+(b-a)/2)
    location_list_new.append(location_list[-1])
    total_nodes=nodes_per_part*(len(location_list_new)-1)   
    
    #initialize array for final nodes.
    nodes=np.zeros(total_nodes)
    
    #np.geomspace(), the function used, generates a concentration about the
    #start of the range, this is why an 'invert' variable is introduced.
    invert=True
    
    #iterate over each segment
    for i in range(len(location_list_new)-1):
        #initialize section start, end and range variables
        sec_start=location_list_new[i]
        sec_end=location_list_new[i+1]
        sec_range=sec_end-sec_start
        #np.geomspace() is used to find the distribution over the desired range
        sec_pos=np.geomspace(ec+offset,sec_range-ec+offset,num=nodes_per_part)
        #the inserted offset is removed to have the range start at ec again
        sec_pos=sec_pos-offset
        start_index=i*nodes_per_part
        
        #Check wether inversion is necessary, if inversion is necessary invert
        #the distribution over the range. 
        #Next add the starting value of the range so the range starts at the
        #segment's starting point instead of at the ec
        #Finally append to nodes list
        if invert==True:
            sec_pos_inv=sec_range-sec_pos[::-1]
            sec_pos_inv=sec_pos_inv[::-1]+sec_start
            sec_pos=sec_pos_inv
            invert=False
        else:
            sec_pos=sec_pos+sec_start
            invert=True
        for o in range(len(sec_pos)):
            nodes[start_index+o]=sec_pos[o]    
    return nodes

B=discretizeCrossSection(h_a, c_a, n_st, 1, t_sk, t_sp, 2, 3, 5)
