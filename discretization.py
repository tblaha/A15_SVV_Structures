# -*- coding: utf-8 -*-
"""
Author: tblaha
Date  : 2019-02-18
"""

from UniversalConstants import *
import numpy as np

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
        
    
    
def discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, nodes_between):
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
    # --- OUTPUTS --- #
    # 1d numpy array: of the x-locations (NOT equally spaced)
    # | x-loc |
    # | 0     |
    # | 15.5  |
    # | ...   |
    
    return 0
    


Bs = discretizeCrossSection(h_a, c_a, n_st, 2)
    