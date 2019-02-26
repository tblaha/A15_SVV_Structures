# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:47:30 2019

@author: Till
"""

from UniversalConstants import *
from Stiffeners import *
import numpy as np


def discretizeCrossSection(S_cor, S_uncor, h_a, c_a, n_st, A_st, t_sk, t_sp, y_c, z_c, booms_between, Ybar_st, cg_correction):
    
    spar_scale_up = 4
    B = np.zeros(( (booms_between+1) * (n_st + spar_scale_up) + n_st, 5))
    
    booms_last_straight = np.floor(booms_between/2)
    
    stiffs_in_circular = 5
    stiffs_in_each_straight = np.floor((n_st - 5) / 2)
    
    length_circular = np.pi * h_a/2
    length_each_straight = np.sqrt((h_a/2)**2 + (c_a - h_a/2)**2)
    
    length_per_stiff = (length_circular + 2*length_each_straight) / n_st
    length_per_boom  = length_per_stiff / (booms_between+1)
    
    
    stiff_leftover_angle  = np.pi/2 - np.arctan2(S_uncor[0,0], S_uncor[0,1])
    angle_per_boom        = (np.arctan2(S_uncor[0,0], S_uncor[0,1]) - np.arctan2(S_uncor[1,0], S_uncor[1,1])) / (booms_between+1)
    leftover_booms        = np.floor(stiff_leftover_angle / angle_per_boom)
    boom_leftover_angle   = stiff_leftover_angle - angle_per_boom*leftover_booms
    
    stiff_leftover_length = stiff_leftover_angle*h_a/2
    boom_leftover_length  = boom_leftover_angle *h_a/2
    
    booms_in_circular = int(stiffs_in_circular + booms_between*(np.floor(stiffs_in_circular/2)*2)+leftover_booms*2)
    
    #2.23009806
    
    s = 0
    for i in range(booms_in_circular):
        angle = stiff_leftover_angle + (i-leftover_booms)*angle_per_boom
        
        B[i,0:2] = h_a/2 * np.array([np.cos(angle), np.sin(angle)]) - np.array([y_c, z_c])
        B[i,4]   = 1
        
        if i: # if not the first boom in this for-loop
            if abs(B[i,1]) > 1e-6: # quick check if not infinite
                # stress ratio reduces to length ratio from neutral line because
                # we assume pure bending with linear variation
                B[i,2]   += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i-1,1]) > 1e-6:
                B[i-1,2] += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i,0]) > 1e-6:
                B[i,3]   += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i-1,0]) > 1e-6:
                B[i-1,3] += t_sk/6 * length_per_boom * (2 + 1)
        
        if not (i-leftover_booms)%(booms_between+1):
            # add stiffener area
            if cg_correction and abs(S_uncor[s,1]-z_c) > 1e-6:
                B[i,2] += A_st * ( (S_cor[s,1]-z_c) / (S_uncor[s,1]-z_c) )**2
            else:
                B[i,2] += A_st
            
            if cg_correction and abs(S_uncor[s,0]-y_c) > 1e-6:
                B[i,3] += A_st * ( (S_cor[s,0]-y_c) / (S_uncor[s,0]-y_c) )**2
            else:
                B[i,3] += A_st 
            
            s = s + 1
        
        # Fix corner cases
        if i == 0: # if first boom
            # (np.pi/2 - angle) * h_a/2 is the arc length from the first boom
            # to the top end of the spar
            B[i,2]  += t_sk/6 * (angle) * h_a/2 * (2 + 1)
            B[i,3]  += t_sk/6 * (angle) * h_a/2 * (2 + 1)
            
        if i == int(booms_in_circular-1): # if last boom
            # (np.pi/2 + angle) * h_a/2 is the arc length from the last boom
            # to the top end of the spar
            B[i,2]  += t_sk/6 * (np.pi - angle) * h_a/2 * (2 + 1)
            B[i,3]  += t_sk/6 * (np.pi - angle) * h_a/2 * (2 + 1)
    
    straight_u_vec = np.array([h_a/2, -c_a+h_a/2]) / length_each_straight
    
    booms_in_straight = int(booms_between - leftover_booms + (booms_between+1)*(stiffs_in_each_straight-1) + booms_last_straight + 1)
    first_boom_length = length_per_boom - boom_leftover_length
    
    for j in range(booms_in_straight):
        i = i + 1
        
        B[i,4]   = 2
        B[i,0:2] = np.array([-h_a/2-y_c,0-z_c])\
                   + straight_u_vec * (first_boom_length + j*length_per_boom)
        
        if j:
            if abs(B[i,1]) > 1e-6: # quick check if not infinite
                # stress ratio reduces to length ratio from neutral line because
                # we assume pure bending with linear variation
                B[i,2]   += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i-1,1]) > 1e-6:
                B[i-1,2] += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i,0]) > 1e-6:
                B[i,3]   += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i-1,0]) > 1e-6:
                B[i-1,3] += t_sk/6 * length_per_boom * (2 + 1)
        
        if not (j+leftover_booms-booms_between)%(booms_between+1):
            # add stiffener area
            if cg_correction and abs(S_uncor[s,1]-z_c) > 1e-6:
                B[i,2] += A_st * ( (S_cor[s,1]-z_c) / (S_uncor[s,1]-z_c) )**2
            else:
                B[i,2] += A_st
            
            if cg_correction and abs(S_uncor[s,0]-y_c) > 1e-6:
                B[i,3] += A_st * ( (S_cor[s,0]-y_c) / (S_uncor[s,0]-y_c) )**2
            else:
                B[i,3] += A_st 
            
            s = s + 1
            
        # Fix corner cases, but only for the last one
        # AM I SURE THAT THERE IS NO CORNER CASE AT THE END OF THIS SECTION         
        if j == 0:
            B[i,2]  += t_sk/6 * first_boom_length * (2 + 1)
            B[i,3]  += t_sk/6 * first_boom_length * (2 + 1)
    k = i
            
    for j in range(booms_in_straight):
        i = i + 1
                
        B[i,4]   = 2
        B[i,0:2] = np.multiply(B[k,0:2], np.array([-1, 1]))
        
        if j:
            if abs(B[i,1]) > 1e-6: # quick check if not infinite
                # stress ratio reduces to length ratio from neutral line because
                # we assume pure bending with linear variation
                B[i,2]   += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i-1,1]) > 1e-6:
                B[i-1,2] += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i,0]) > 1e-6:
                B[i,3]   += t_sk/6 * length_per_boom * (2 + 1)
            if abs(B[i-1,0]) > 1e-6:
                B[i-1,3] += t_sk/6 * length_per_boom * (2 + 1)
        
        if not (j-booms_last_straight)%(booms_between+1):
            # add stiffener area
            if cg_correction and abs(S_uncor[s,1]-z_c) > 1e-6:
                B[i,2] += A_st * ( (S_cor[s,1]-z_c) / (S_uncor[s,1]-z_c) )**2
            else:
                B[i,2] += A_st
            
            if cg_correction and abs(S_uncor[s,0]-y_c) > 1e-6:
                B[i,3] += A_st * ( (S_cor[s,0]-y_c) / (S_uncor[s,0]-y_c) )**2
            else:
                B[i,3] += A_st 
            
            s = s + 1
        
        k = k - 1
        
        # Fix corner cases, but only for the last one
        # AM I SURE THAT THERE IS NO CORNER CASE AT THE START OF THIS SECTION         
        if j == int(booms_in_straight)-1:
            B[i,2]  += t_sk/6 * first_boom_length * (2 + 1)
            B[i,3]  += t_sk/6 * first_boom_length * (2 + 1)
        
        
    # ----- booms in spar ----- #
    for l in range(booms_between*spar_scale_up+2): # the two comes from the top and bottom ends
        i = i + 1
        
        # walk down from the top (h_a/2) to the bottom (-h_a+h_a/2)
        B[i, 0:2] = np.array([ -l * h_a / (booms_between*spar_scale_up+1) + h_a/2 -y_c, 0-z_c] )
        
        # we call the spar section 3
        B[i,4]    = 3
        
        #just like above, skin contributions
        if l:
            B[i,2]   += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
            B[i-1,2] += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
            B[i,3]   += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
            B[i-1,3] += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
        
        # no stiffeners in here
        
        # top corner case        
        if l == 0:
            B[i,2]   += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
            B[i,3]   += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
          
        # bottom corner case
        if l == booms_between*spar_scale_up+2-1:
            B[i,2]   += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
            B[i,3]   += t_sp/6 * h_a/(booms_between*spar_scale_up+1) * (2 + 1)
            
            
            
    # shitty postfix
    emtpy_lines = int(np.floor(len(B[np.where(B[:,0:2] == 0)])/2))
    B = np.delete(B, [np.arange(len(B)-emtpy_lines,len(B))],0)
    
    
    
    B[:,0:2] = B[:,0:2] + np.array([y_c, z_c])
    
    return B


def plotCrossSection(B, Balt):
    # plots the 2 cross sectional discretization for verification
    #
    # --- INPUTS --- #
    # B: the boom array
    #
    # --- OUTPUTS --- #
    # none

    import matplotlib.pyplot as plt
    
    # two subplots (first for bending around y, second for z)
    fig, axs = plt.subplots(2, 1)
    
    # size
    si = B.shape;
    if si[1] == 5:
        # put down the scatter with the area as the size argument
        axs[0].scatter(B[:,1], B[:,0], B[:,2])
        axs[1].scatter(B[:,1], B[:,0], B[:,3])
        axs[0].scatter(Balt[:,1], Balt[:,0], Balt[:,2])
        axs[1].scatter(Balt[:,1], Balt[:,0], Balt[:,3])
    else:
        axs[0].scatter(B[:,1], B[:,0])
        axs[1].scatter(B[:,1], B[:,0])
        axs[0].scatter(Balt[:,1], Balt[:,0])
        axs[1].scatter(Balt[:,1], Balt[:,0])
        
    
    # format: axis equal and invert the z axis (x-axis in the plot referece frame)
    axs[0].axis('equal')
    axs[1].axis('equal')
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    
    # make pretty
    fig.tight_layout()
    
    # show
    plt.show()
      
    
S_uncor = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 0)
S_cor   = generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 1)
#
#for i in range(32,-1,-4):
bib = 49
B = discretizeCrossSection(S_cor, S_uncor, h_a, c_a, n_st, A_st, t_sk, t_sp, 0, -98, bib, Ybar_st, 0)
Balt = discretizeCrossSection(S_cor, S_uncor, h_a, c_a, n_st, A_st, t_sk, t_sp, 0, -98, bib, Ybar_st, 1)
plotCrossSection(B, Balt)

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
    #Points of interest
    location_list=[x_h1,x_h2-(d_a/2),x_h2,x_h2+(d_a/2),x_h3,l_a]
    location_list_new=[0]
    for i in range(len(location_list)-2):
        location_list_new.append(location_list[i])
        a=location_list[i]
        b=location_list[i+1]
        location_list_new.append(a+((b-a)/2))
    location_list_new.append(x_h3)
    location_list_new.append(l_a)
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
        sec_length=sec_end-sec_start
        #np.geomspace() is used to find the distribution over the desired range
        distr=np.geomspace(ec+offset,sec_length+offset-ec,num=nodes_per_part)
        #the inserted offset is removed to have the range start at ec again
        sec_distr=distr-offset 

        #Check wether inversion is necessary, if inversion is necessary invert
        #the distribution over the range. 
        #Next add the starting value of the range so the range starts at the
        #segment's starting point instead of at the ec
        #Finally append to nodes list
        if invert==True:
            sec_distr_inv=sec_length-sec_distr[::-1]
            sec_pos=sec_distr_inv+sec_start
            invert=False
        else:
            sec_pos=sec_distr+sec_start
            invert=True
            
#       Debugging code:
#        print('sec properties: Sec_start:',sec_start,'Sec_end:',sec_end,\
#        'sec_pos[1] and [-1]:',sec_pos[1],',',sec_pos[-1],'invert=',invert)
    
        #add section to nodes list
        start_index=i*nodes_per_part
        for o in range(len(sec_pos)):
            nodes[start_index+o]=sec_pos[o]
    return nodes