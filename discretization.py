# -*- coding: utf-8 -*-
"""
Author: tblaha
Date  : 2019-02-18
"""

from UniversalConstants import *
import numpy as np

import matplotlib.pyplot as plt

def discretizeCrossSection(h_a, c_a, n_st, booms_between):
    # Takes the geometry, the number of stiffeners and the number of booms in
    # between each stiffener and compute boom locations and areas
    #
    # --- INPUTS --- #
    # h_a                 : height of aileron (float)
    # c_a                 : chord length of aileron (float)
    # n_st                : The amount of equally spaced stiffeners along the
    #                       perimiter of the skin panels (int)
    # booms_between       : The amount of booms in between stiffeners; 
    #                       stiffeners themselves are automatically booms (int)
    # --- OUTPUTS --- #
    # 2d numpy array:
    # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # cell id: 1 (exclusively left cell, clockwise sorted)
    #          2 (exclusively right cell, clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    
    # we know that there are n_st+booms_between*(n_st+1) booms, so we can
    # iterate over that range and figure out each boom
    Bs = np.zeros((n_st+booms_between*(n_st+1), 5))
    
    # Find total arc length of the semi circle
    sc_arc_length = h_a*np.pi/2
    
    # Total length of the 2 straight sections
    straight_length = 2*np.sqrt(h_a**2 + (c_a-h_a)**2)
    
    # Total length
    total_length = sc_arc_length + straight_length
    
    # length per segment
    length_per_segment = total_length/(n_st+1)
    
    # stiffeners in the circular segment
    stiffs_circular = np.floor(sc_arc_length/length_per_segment)
    
    # booms in circular section
    for i in range(int(stiffs_circular)):
        unit_angle = (2 - i) * length_per_segment/(2*sc_arc_length) * 2*np.pi;
        Bs[i,0]    = np.sin(unit_angle)*h_a/2
        Bs[i,1]    = np.cos(unit_angle)*h_a/2
        
        
        
    return  Bs
        
    
    
def discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, nodes_between=50,ec=0.0001,offset=30,):
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

