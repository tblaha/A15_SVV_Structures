# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


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
    
    
    