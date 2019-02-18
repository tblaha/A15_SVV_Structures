# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *
import numpy as np

def discretizeCrossSection(number_of_stiffeners, booms_between):
    # Takes the geometry, the number of stiffeners and the number of booms in
    # between each stiffener and compute boom locations and areas
    # --- INPUTS --- #
    # !!! some more geometric parameters will be added in the future !!!
    # number_of_stiffeners: The amount of equally spaced stiffeners along the
    #                       perimiter of the skin panels
    # booms_between       : The amount of booms in between stiffeners; 
    #                       stiffeners themselves are automatically booms
    
    # --- OUTPUTS --- #
    # 2d numpy array:
    # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # cell id: 1 (exclusively left cell, clockwise sorted)
    #          2 (exclusively right cell, clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    
    
    
def discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, nodes_between):
    # Takes the spanwise characteristics of the aileron and computes a
    # discretization at which the deflection of leading edge and trailing edge
    # will be computed later. Spanwise nodes (the x-location of the discrete
    # cross sections) are closer to spanwise items like ribs and actuators,
    # since a lot of the stresses
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
    #
    # Concentrations of nodes will exist aruond x_h1, x_h2, x_h3, x_h2+/-d_a
    # Sections: 0 to x_h1, x_h1 to x_h2-da, x_h2-da to x_h2, x_h2 to x_h2+da,
    # x_h2+da to x_h3, x_h3 to l_a
    # adding one hundreth mm at the start, removing one at the end to
    # prevent overlap
    location_list=[0,x_h1,x_h2-d_a,x_h2,x_h2+d_a,l_a]
    total_nodes=nodes_between*4
    nodes_per_part=nodes_between/2
    nodes=numpy.zeros[8*nodes_between]
    for i in range(len(location_list)-1):
        sec_start=location_list[i]
        sec_end=location_list[i+1]
        sec_pos=np.logspace(sec_start,sec_end
    