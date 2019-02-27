# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:30:26 2019

@author: Till
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt


def InterpretFEM(h_a, c_a):
    plt.ioff()
    ###########################
    ### Get nodal locations ###
    ###########################
    
    nodes   = np.genfromtxt('FEMData/NodeLocations.txt', delimiter=',')
    numnodes = int(np.max(nodes[:,0]))
    
    nodes_ribA = np.array([12,  13,  15,  26, 188, 189, 190, 191, 192, 193, 244, 245, 246, 247, 248, 249,\
     731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746,\
     747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762,\
     763, 764, 792, 793, 794, 795, 796, 797, 798, 799]).astype('int')
    
    nodes_ribB = np.array([ 9,  10,  24,  25, 172, 173, 174, 175, 176, 177, 587, 588, 589, 590, 591, 592,\
     593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 617, 618, 619, 620, 621,\
     622, 623, 624, 630, 631, 632, 633, 634, 635, 675, 676, 677, 678, 679, 680, 681,\
     682, 683, 684, 685, 686, 687, 688, 689, 690, 691]).astype('int')
    
    nodes_ribC = np.array([5,   6,  20,  21,  96,  97,  98,  99, 100, 101, 346, 347, 348, 349, 350, 351,\
     352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 432, 433, 434, 435, 436,\
     437, 438, 439, 514, 515, 516, 517, 518, 519, 531, 532, 533, 534, 535, 536, 537,\
     538, 539, 540, 541, 542, 543, 544, 545, 546, 547]).astype('int')
    
    nodes_ribD = np.array([2,   3,  16,  17,  32,  33,  34,  35,  36,  37, 289, 290, 291, 292, 293, 294,\
     295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 329, 330, 331, 332, 333,\
     334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 418, 419, 420, 421,\
     422, 423, 424, 425, 426, 427, 428, 429, 430, 431]).astype('int')
    
    nodes_ribs = np.zeros((4, len(nodes_ribA)))
    nodes_ribs[0,:] = nodes_ribA
    nodes_ribs[1,:] = nodes_ribB
    nodes_ribs[2,:] = nodes_ribC
    nodes_ribs[3,:] = nodes_ribD
    
    nodes_ribs_sort = np.zeros(np.shape(nodes_ribs))
    
    # get and sort leading and trailing edge nodes
    nodes_TE  = nodes[np.where(nodes[:,3] == -c_a+h_a/2), :][0]
    nodes_TE  = nodes_TE[nodes_TE[:,1].argsort(),:]
    nodes_LE  = nodes[np.where(nodes[:,3] == h_a/2), :][0]
    nodes_LE  = nodes_LE[nodes_LE[:,1].argsort(),:]
    
    
    
    
    ##############################
    ### Get von Mises Stresses ###
    ##############################
    
    line_ranges = np.array([[24, 8087], [8109, 12140], [12162, 18433], [18455, 26518]])
    diff_lines  = (np.diff(line_ranges,1,1)+1)
    cum_lines   = np.cumsum(diff_lines)
    total_lines = np.sum(diff_lines)
    
    # prealloc
    S_up_L    = np.zeros((total_lines, 3))
    S_up_nL   = np.zeros((total_lines, 3))
    S_down_L  = np.zeros((total_lines, 3))
    S_down_nL = np.zeros((total_lines, 3))
    
    # up, with loads
    S_up_L[0:cum_lines[0]]            = np.genfromtxt('FEMData/A320_SLC1.rpt', skip_header=line_ranges[0,0]-1, max_rows=diff_lines[0,0])[:,[1,2,3]]
    S_up_L[cum_lines[0]:cum_lines[1]] = np.genfromtxt('FEMData/A320_SLC1.rpt', skip_header=line_ranges[1,0]-1, max_rows=diff_lines[1,0])[:,[1,2,3]]
    S_up_L[cum_lines[1]:cum_lines[2]] = np.genfromtxt('FEMData/A320_SLC1.rpt', skip_header=line_ranges[2,0]-1, max_rows=diff_lines[2,0])[:,[1,2,3]]
    S_up_L[cum_lines[2]:]             = np.genfromtxt('FEMData/A320_SLC1.rpt', skip_header=line_ranges[3,0]-1, max_rows=diff_lines[3,0])[:,[1,2,3]]
    S_up_L = S_up_L[S_up_L[:,0].argsort(),:]
    
    # up, without loads
    S_up_nL[0:cum_lines[0]]            = np.genfromtxt('FEMData/A320_SR1.rpt', skip_header=line_ranges[0,0]-1, max_rows=diff_lines[0,0])[:,[1,2,3]]
    S_up_nL[cum_lines[0]:cum_lines[1]] = np.genfromtxt('FEMData/A320_SR1.rpt', skip_header=line_ranges[1,0]-1, max_rows=diff_lines[1,0])[:,[1,2,3]]
    S_up_nL[cum_lines[1]:cum_lines[2]] = np.genfromtxt('FEMData/A320_SR1.rpt', skip_header=line_ranges[2,0]-1, max_rows=diff_lines[2,0])[:,[1,2,3]]
    S_up_nL[cum_lines[2]:]             = np.genfromtxt('FEMData/A320_SR1.rpt', skip_header=line_ranges[3,0]-1, max_rows=diff_lines[3,0])[:,[1,2,3]]
    S_up_nL = S_up_nL[S_up_nL[:,0].argsort(),:]
    
    # down, with loads
    S_down_L[0:cum_lines[0]]            = np.genfromtxt('FEMData/A320_SLC2.rpt', skip_header=line_ranges[0,0]-1, max_rows=diff_lines[0,0])[:,[1,2,3]]
    S_down_L[cum_lines[0]:cum_lines[1]] = np.genfromtxt('FEMData/A320_SLC2.rpt', skip_header=line_ranges[1,0]-1, max_rows=diff_lines[1,0])[:,[1,2,3]]
    S_down_L[cum_lines[1]:cum_lines[2]] = np.genfromtxt('FEMData/A320_SLC2.rpt', skip_header=line_ranges[2,0]-1, max_rows=diff_lines[2,0])[:,[1,2,3]]
    S_down_L[cum_lines[2]:]             = np.genfromtxt('FEMData/A320_SLC2.rpt', skip_header=line_ranges[3,0]-1, max_rows=diff_lines[3,0])[:,[1,2,3]]
    S_down_L = S_down_L[S_down_L[:,0].argsort(),:]
    
    # down, without loads
    S_down_nL[0:cum_lines[0]]            = np.genfromtxt('FEMData/A320_SR2.rpt', skip_header=line_ranges[0,0]-1, max_rows=diff_lines[0,0])[:,[1,2,3]]
    S_down_nL[cum_lines[0]:cum_lines[1]] = np.genfromtxt('FEMData/A320_SR2.rpt', skip_header=line_ranges[1,0]-1, max_rows=diff_lines[1,0])[:,[1,2,3]]
    S_down_nL[cum_lines[1]:cum_lines[2]] = np.genfromtxt('FEMData/A320_SR2.rpt', skip_header=line_ranges[2,0]-1, max_rows=diff_lines[2,0])[:,[1,2,3]]
    S_down_nL[cum_lines[2]:]             = np.genfromtxt('FEMData/A320_SR2.rpt', skip_header=line_ranges[3,0]-1, max_rows=diff_lines[3,0])[:,[1,2,3]]
    S_down_nL = S_down_nL[S_down_nL[:,0].argsort(),:]
    
    
    
    
    
    
    #############################
    ### Get displacement data ###
    #############################
    
    header_lines_U = 19
    
    # up, with loads
    U_up_L = np.genfromtxt('FEMData/A320_ULC1.rpt', skip_header=header_lines_U, max_rows=numnodes)[:,[0,6,7,8]]
    
    # up, without loads
    U_up_nL = np.genfromtxt('FEMData/A320_UR1.rpt',  skip_header=header_lines_U, max_rows=numnodes)[:,[0,6,7,8]]
    
    # down, with loads
    U_down_L = np.genfromtxt('FEMData/A320_ULC2.rpt',  skip_header=header_lines_U, max_rows=numnodes)[:,[0,6,7,8]]
    
    # down, without loads
    U_down_nL = np.genfromtxt('FEMData/A320_UR2.rpt',  skip_header=header_lines_U, max_rows=numnodes)[:,[0,6,7,8]]
    
    
    
    
    
    
    
    
    
    
    ##########################
    ### Post proc stresses ###
    ##########################
    
    S_up_L_post    = np.zeros((numnodes, 2))
    S_up_nL_post   = np.zeros((numnodes, 2))
    S_down_L_post  = np.zeros((numnodes, 2))
    S_down_nL_post = np.zeros((numnodes, 2))
    
    S_up_L_post[:,0]    = range(1, 1+numnodes)
    S_up_nL_post[:,0]   = range(1, 1+numnodes)
    S_down_L_post[:,0]  = range(1, 1+numnodes)
    S_down_nL_post[:,0] = range(1, 1+numnodes)
    
    for i in range(1, 1+numnodes):
        S_up_L_post[i-1,1]    = np.mean(S_up_L   [np.where(S_up_L   [:,0] == i), 1:][0])*1e3
        S_up_nL_post[i-1,1]   = np.mean(S_up_nL  [np.where(S_up_nL  [:,0] == i), 1:][0])*1e3
        S_down_L_post[i-1,1]  = np.mean(S_down_L [np.where(S_down_L [:,0] == i), 1:][0])*1e3
        S_down_nL_post[i-1,1] = np.mean(S_down_nL[np.where(S_down_nL[:,0] == i), 1:][0])*1e3
        
    
    ### assign to ribs ###
    
    arc_coords = np.zeros(np.shape(nodes_ribs))
    
    # sort ribs
    i = 0
    for nodes_rib in nodes_ribs:
        nodes_rib_tmp = nodes[nodes_rib.astype('int')-1]
        num           = len(nodes_rib_tmp[:,0])
        
        cutoff = 1e-12
    
        left = nodes_rib_tmp[:,3] > cutoff*np.ones((num))
        right = nodes_rib_tmp[:,3] < -cutoff*np.ones((num))
        top = nodes_rib_tmp[:,2] > cutoff*np.ones((num))
        bottom = nodes_rib_tmp[:,2] < -cutoff*np.ones((num))
        in_spar=  abs(nodes_rib_tmp[:,3]) < 1e-12*np.ones((num))
    
        left         = nodes_rib_tmp[left]
        left         = np.flipud(left[left[:,2].argsort(),:])
        right_bottom = nodes_rib_tmp[right * bottom]
        right_bottom = right_bottom[right_bottom[:,2].argsort(),:]
        right_top    = nodes_rib_tmp[right * top]
        right_top    = right_top[right_top[:,2].argsort(),:]
        spar         = nodes_rib_tmp[in_spar]
        spar         = np.flipud(spar[spar[:,2].argsort(),:])
    
        nodes_rib_sort = np.zeros(num)
        nodes_amounts = [len(left), len(right_bottom), len(right_top), len(spar)]
        cum_nodes     = np.cumsum(nodes_amounts)    
        
        nodes_rib_sort[0           :cum_nodes[0]] = left[:,0]
        nodes_rib_sort[cum_nodes[0]:cum_nodes[1]] = right_bottom[:,0]
        nodes_rib_sort[cum_nodes[1]:cum_nodes[2]] = right_top[:,0]
        nodes_rib_sort[cum_nodes[2]:cum_nodes[3]] = spar[:,0]
        nodes_rib_sort = nodes_rib_sort.astype('int')
        
        nodes_ribs_sort[i] = nodes_rib_sort
        
        j = 0
        for node in nodes_rib_sort:
            if j < len(left):
                # circular section
                arc_coords[i,j] = h_a/2 * np.arctan2(nodes[node-1, 3], nodes[node-1, 2])
            elif j < len(left) + len(right_bottom):
                arc_coords[i,j] = np.pi * h_a/2 + np.linalg.norm(nodes[node-1, 2:] - np.array([-h_a/2, 0]))
            elif j < len(left) + len(right_bottom) + len(right_top):
                arc_coords[i,j] = np.pi * h_a/2 + np.linalg.norm(np.array([h_a/2, c_a-h_a/2]))\
                                                + np.linalg.norm(nodes[node-1, 2:] - np.array([0, -c_a+h_a/2]))
            else:
                arc_coords[i,j] = np.pi * h_a/2 + np.linalg.norm(np.array([h_a/2, c_a-h_a/2]))*2\
                                                - nodes[node-1, 2] + h_a/2
            
            j = j + 1
            
        
        i = i + 1
    
        
    S_up_L_post_ribA = S_up_L_post[nodes_ribs_sort[0].astype('int')-1, 1]
    S_up_L_post_ribB = S_up_L_post[nodes_ribs_sort[1].astype('int')-1, 1]
    S_up_L_post_ribC = S_up_L_post[nodes_ribs_sort[2].astype('int')-1, 1]
    S_up_L_post_ribD = S_up_L_post[nodes_ribs_sort[3].astype('int')-1, 1]
    S_up_L_post_ribs = np.zeros((4,num))
    S_up_L_post_ribs[0,:] = S_up_L_post_ribA
    S_up_L_post_ribs[1,:] = S_up_L_post_ribB
    S_up_L_post_ribs[2,:] = S_up_L_post_ribC
    S_up_L_post_ribs[3,:] = S_up_L_post_ribD
    
    S_up_nL_post_ribA = S_up_nL_post[nodes_ribs_sort[0].astype('int')-1, 1]
    S_up_nL_post_ribB = S_up_nL_post[nodes_ribs_sort[1].astype('int')-1, 1]
    S_up_nL_post_ribC = S_up_nL_post[nodes_ribs_sort[2].astype('int')-1, 1]
    S_up_nL_post_ribD = S_up_nL_post[nodes_ribs_sort[3].astype('int')-1, 1]
    
    S_down_L_post_ribA = S_down_L_post[nodes_ribs_sort[0].astype('int')-1, 1]
    S_down_L_post_ribB = S_down_L_post[nodes_ribs_sort[1].astype('int')-1, 1]
    S_down_L_post_ribC = S_down_L_post[nodes_ribs_sort[2].astype('int')-1, 1]
    S_down_L_post_ribD = S_down_L_post[nodes_ribs_sort[3].astype('int')-1, 1]
    
    S_down_nL_post_ribA = S_down_nL_post[nodes_ribs_sort[0].astype('int')-1, 1]
    S_down_nL_post_ribB = S_down_nL_post[nodes_ribs_sort[1].astype('int')-1, 1]
    S_down_nL_post_ribC = S_down_nL_post[nodes_ribs_sort[2].astype('int')-1, 1]
    S_down_nL_post_ribD = S_down_nL_post[nodes_ribs_sort[3].astype('int')-1, 1]
    
    
    
    
    
    #######################
    ### von Mises plots ###
    #######################
    
    
    # scatters
    plt.figure(0, figsize=(7.5, 4.5))
    axs = plt.axes()
    plt.scatter(nodes[nodes_ribs_sort[0].astype('int')-1,3], nodes[nodes_ribs_sort[0].astype('int')-1,2], c=S_up_L_post_ribA, cmap='jet')
    plt.title('Validation Data -- von Mises Rib A -- Maximum: %.2f MPa' % np.max(S_up_L_post_ribA))
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    axs.invert_xaxis()
    plt.tight_layout
    cbar = plt.colorbar()
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    plt.savefig('Plots/LC1_RibA_scatter.eps', format='eps')
    
    plt.figure(1, figsize=(7.5, 4.5))
    axs = plt.axes()
    plt.scatter(nodes[nodes_ribs_sort[1].astype('int')-1,3], nodes[nodes_ribs_sort[1].astype('int')-1,2], c=S_up_L_post_ribB, cmap='jet')
    plt.title('Validation Data -- von Mises Rib B -- Maximum: %.2f MPa' % np.max(S_up_L_post_ribB))
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    axs.invert_xaxis()
    plt.tight_layout
    cbar = plt.colorbar()
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    plt.savefig('Plots/LC1_RibB_scatter.eps', format='eps')
    
    plt.figure(2, figsize=(7.5, 4.5))
    axs = plt.axes()
    plt.scatter(nodes[nodes_ribs_sort[2].astype('int')-1,3], nodes[nodes_ribs_sort[2].astype('int')-1,2], c=S_up_L_post_ribC, cmap='jet')
    plt.title('Validation Data -- von Mises Rib C -- Maximum: %.2f MPa' % np.max(S_up_L_post_ribC))
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    axs.invert_xaxis()
    plt.tight_layout
    cbar = plt.colorbar()
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    plt.savefig('Plots/LC1_RibC_scatter.eps', format='eps')
    
    plt.figure(3, figsize=(7.5, 4.5))
    axs = plt.axes()
    plt.scatter(nodes[nodes_ribs_sort[3].astype('int')-1,3], nodes[nodes_ribs_sort[3].astype('int')-1,2], c=S_up_L_post_ribD, cmap='jet')
    plt.title('Validation Data -- von Mises Rib D -- Maximum: %.2f MPa' % np.max(S_up_L_post_ribD))
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    axs.invert_xaxis()
    plt.tight_layout
    cbar = plt.colorbar()
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    plt.savefig('Plots/LC1_RibD_scatter.eps', format='eps')
    
    
    #plt.figure(4)
    #axs = plt.axes()
    #plt.plot(arc_coords[0], S_up_L_post_ribA, '-x')
    #plt.xlabel('Tangential Coordinate (traversing CCW) [mm]')
    #plt.ylabel('Von Mises Stress [MPa]')
    #plt.title('Rib A: Maximum von Mises: %.2f MPa' % np.max(S_up_L_post_ribA))
    #plt.tight_layout
    
    
    # lines
    
    
    
    ########################
    ### Deflection Plots ###
    ########################
    
    
    ### Trailing Edge ###
    
    TE_xlocs = nodes_TE[:,1]
    U_up_L_TE  = U_up_L [nodes_TE[:,0].astype('int')-1, :][:,[1,2,3]]
    U_up_nL_TE = U_up_nL[nodes_TE[:,0].astype('int')-1, :][:,[1,2,3]]
    
    U_down_L_TE  = U_down_L [nodes_TE[:,0].astype('int')-1, :][:,[1,2,3]]
    U_down_nL_TE = U_down_nL[nodes_TE[:,0].astype('int')-1, :][:,[1,2,3]]
    
    
    plt.figure(10, figsize=(8, 6))
    axs = plt.axes()
    plt.subplot(211)
    plt.title('Validation Data -- Global Trailing Edge Deflection -- Maximum: %.2f mm' % np.max(U_up_nL_TE[:,1]))
    plt.ylabel('y-displacement [mm]')
    plt.plot(TE_xlocs, U_up_nL_TE[:,1], '-')
    plt.plot(TE_xlocs, U_up_L_TE[:,1], '-.')
    plt.legend(['without loads', 'with actuator and aero loads'])
    
    plt.subplot(212)
    plt.xlabel('x location (spanwise) [mm]')
    plt.ylabel('z-displacement [mm]')
    plt.plot(TE_xlocs, U_up_nL_TE[:,2])
    plt.plot(TE_xlocs, U_up_L_TE[:,2], '-.')
    
    plt.savefig('Plots/LC1_U_TE.eps', format='eps')
    
    
    correction_up = -26/180*np.pi * (c_a-h_a/2)
    
    plt.figure(11, figsize=(8, 6))
    axs = plt.axes()
    plt.subplot(211)
    plt.ylabel('y-displacement [mm]')
    plt.title('De-rotated Validation Data -- Global Trailing Edge Deflection -- Maximum: %.2f mm' % (np.max(U_up_nL_TE[:,1]) + correction_up))
    plt.plot(TE_xlocs, U_up_nL_TE[:,1] + correction_up)
    plt.plot(TE_xlocs, U_up_L_TE[:,1] + correction_up, '-.')
    plt.legend(['without loads', 'with actuator and aero loads'])
    
    plt.subplot(212)
    plt.xlabel('x location (spanwise) [mm]')
    plt.ylabel('z-displacement [mm]')
    plt.plot(TE_xlocs, U_up_nL_TE[:,2])
    plt.plot(TE_xlocs, U_up_L_TE[:,2], '-.')
    
    plt.savefig('Plots/LC1_U_TE_derot.eps', format='eps')
    
    
    
    ### Leading Edge ###
    
    LE_xlocs = nodes_LE[:,1]
    U_up_L_LE  = U_up_L [nodes_LE[:,0].astype('int')-1, :][:,[1,2,3]]
    U_up_nL_LE = U_up_nL[nodes_LE[:,0].astype('int')-1, :][:,[1,2,3]]
    
    U_down_L_LE  = U_down_L [nodes_LE[:,0].astype('int')-1, :][:,[1,2,3]]
    U_down_nL_LE = U_down_nL[nodes_LE[:,0].astype('int')-1, :][:,[1,2,3]]
    
    
    plt.figure(12, figsize=(8, 6))
    axs = plt.axes()
    plt.subplot(211)
    plt.ylabel('y-displacement [mm]')
    plt.title('Validation Data -- Global Leading Edge Deflection -- Maximum: %.2f mm' % np.max(U_up_nL_LE[:,1]))
    plt.plot(LE_xlocs, U_up_nL_LE[:,1])
    plt.plot(LE_xlocs, U_up_L_LE[:,1], '-.')
    plt.legend(['without loads', 'with actuator and aero loads'])
    
    plt.subplot(212)
    plt.xlabel('x location (spanwise) [mm]')
    plt.ylabel('z-displacement [mm]')
    plt.plot(LE_xlocs, U_up_nL_LE[:,2])
    plt.plot(LE_xlocs, U_up_L_LE[:,2], '-.')
    
    plt.savefig('Plots/LC1_U_LE.eps', format='eps')
    
    #plt.subplot(222)
    #plt.plot(TE_xlocs, U_down_nL_TE[:,1])
    #plt.plot(TE_xlocs, U_down_L_TE[:,1])
    #
    #plt.subplot(224)
    #plt.plot(TE_xlocs, U_down_nL_TE[:,2])
    #plt.plot(TE_xlocs, U_down_L_TE[:,2])
    
    correction_up = 26/180*np.pi * (h_a/2)
    
    plt.figure(13, figsize=(8, 6))
    axs = plt.axes()
    plt.subplot(211)
    plt.ylabel('y-displacement [mm]')
    plt.title('De-rotated Validation Data -- Global Leading Edge Deflection -- Maximum: %.2f mm' % (np.max(U_up_nL_LE[:,1]) + correction_up))
    plt.plot(LE_xlocs, U_up_nL_LE[:,1] + correction_up)
    plt.plot(LE_xlocs, U_up_L_LE[:,1] + correction_up, '-.')
    plt.legend(['without loads', 'with actuator and aero loads'])
    
    plt.subplot(212)
    plt.xlabel('x location (spanwise) [mm]')
    plt.ylabel('z-displacement [mm]')
    plt.plot(LE_xlocs, U_up_nL_LE[:,2])
    plt.plot(LE_xlocs, U_up_L_LE[:,2], '-.')
    
    
    plt.savefig('Plots/LC1_U_LE_derot.eps', format='eps')
    
    
    
    plt.ion()

    return arc_coords, S_up_L_post_ribs



arc_coordinates, vonMises_ribs = InterpretFEM(h_a, c_a)










