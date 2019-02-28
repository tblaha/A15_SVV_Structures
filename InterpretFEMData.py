# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:30:26 2019

@author: Till
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt


def InterpretFEM(h_a, c_a, version=''):
    
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
    

    
    ##############################
    ### Get von Mises Stresses ###
    ##############################
    
    S_post_ribs    = np.zeros(( 2, 4, len(nodes_ribA) ))
    arc_coords     = np.zeros(( 2, 4, len(nodes_ribA) ))
    nodes_ribA_xyz = np.zeros(( 4, len(nodes_ribA), 4 ))
    
    # up loads
    arc_coords[0,0], S_post_ribs[0,0], nodes_ribA_xyz[0] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SLC1' + version + '.rpt', nodes, nodes_ribA)
    arc_coords[0,1], S_post_ribs[0,1], nodes_ribA_xyz[1] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SLC1' + version + '.rpt', nodes, nodes_ribB)
    arc_coords[0,2], S_post_ribs[0,2], nodes_ribA_xyz[2] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SLC1' + version + '.rpt', nodes, nodes_ribC)
    arc_coords[0,3], S_post_ribs[0,3], nodes_ribA_xyz[3] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SLC1' + version + '.rpt', nodes, nodes_ribD)
    
    # up no loads
    arc_coords[1,0], S_post_ribs[1,0], nodes_ribA_xyz[0] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SR1' + version + '.rpt', nodes, nodes_ribA)
    arc_coords[1,1], S_post_ribs[1,1], nodes_ribA_xyz[1] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SR1' + version + '.rpt', nodes, nodes_ribB)
    arc_coords[1,2], S_post_ribs[1,2], nodes_ribA_xyz[2] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SR1' + version + '.rpt', nodes, nodes_ribC)
    arc_coords[1,3], S_post_ribs[1,3], nodes_ribA_xyz[3] = getFEMSection(-1, h_a, c_a, 'FEMData/A320_SR1' + version + '.rpt', nodes, nodes_ribD)
    
    
    
    ### plotting ###
    for i in range(2):
        for j in range(4):
            if j == 0:
                rib_name = 'A'
            elif j == 1:
                rib_name = 'B'
            elif j == 2:
                rib_name = 'C'
            elif j == 3:
                rib_name = 'D'
            
            if i == 0:
                # loads
                title = 'Validation -- von Mises Rib ' + rib_name + ' -- All Loads'
                filename = 'S_LC1_Rib' + rib_name + version + '_scatter_FEM'
            else:
                title = 'Validation -- von Mises Rib ' + rib_name + ' -- No loads'
                filename = 'S_R1_Rib' + rib_name + version + '_scatter_FEM'
                
            plotFEMSection(nodes_ribA_xyz[j], S_post_ribs[i,j], title, filename)
    
    
    ##################
    ### Deflection ###
    ##################
        
    
    ### plotting ###
    U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE = getLETE(h_a, c_a, nodes, 'FEMData/A320_', version)
    plotLETE(U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE, version, span_disc = [], U_LE_Model=[], U_TE_Model=[])
    

    return arc_coords, S_post_ribs, U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE














### helper functions ###
    




def getLETE(h_a, c_a, nodes, filename_pre, version=''):
    
    
    numnodes = len(nodes)
    ##################
    ### Deflection ###
    ##################
    
    # get and sort leading and trailing edge nodes
    nodes_LE  = nodes[np.where(nodes[:,3] == h_a/2), :][0]
    nodes_LE  = nodes_LE[nodes_LE[:,1].argsort(),:]
    nodes_TE  = nodes[np.where(nodes[:,3] == -c_a+h_a/2), :][0]
    nodes_TE  = nodes_TE[nodes_TE[:,1].argsort(),:]
            
    
    
    header_lines_U = 19
    
    # up, with loads
    U_up_L = np.genfromtxt(filename_pre + 'ULC1' + version + '.rpt', skip_header=header_lines_U, max_rows=numnodes)[:,[0,6,7,8]]
    
    # up, without loads
    U_up_nL = np.genfromtxt(filename_pre + 'UR1' + version + '.rpt',  skip_header=header_lines_U, max_rows=numnodes)[:,[0,6,7,8]]
        
    
    
    ### Trailing Edge ###
    TE_xlocs = nodes_TE[:,1]
    U_up_L_TE  = U_up_L [nodes_TE[:,0].astype('int')-1, :][:,[1,2,3]]
    U_up_nL_TE = U_up_nL[nodes_TE[:,0].astype('int')-1, :][:,[1,2,3]]
    
    the_shape = np.shape(U_up_L_TE)
    U_TEs_FEM = np.zeros((2, the_shape[0], the_shape[1]))
    
    U_TEs_FEM[0] = U_up_L_TE
    U_TEs_FEM[1] = U_up_nL_TE
    
    
    
    
    
    ### Leading Edge ###
    LE_xlocs = nodes_LE[:,1]
    U_up_L_LE  = U_up_L [nodes_LE[:,0].astype('int')-1, :][:,[1,2,3]]
    U_up_nL_LE = U_up_nL[nodes_LE[:,0].astype('int')-1, :][:,[1,2,3]]
    
    the_shape = np.shape(U_up_L_LE)
    U_LEs_FEM = np.zeros((2, the_shape[0], the_shape[1]))
    
    U_LEs_FEM[0] = U_up_L_LE
    U_LEs_FEM[1] = U_up_nL_LE
    
    correction_LE = 26/180*np.pi * (h_a/2)
    correction_TE = -26/180*np.pi * (c_a-h_a/2)
    
    
    
    return U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE
    






def plotLETE(U_LEs_FEM, U_TEs_FEM, LE_xlocs, TE_xlocs, correction_LE, correction_TE, version = '', span_disc = [], U_LE_Model=[], U_TE_Model=[]):
    ########################
    ### Deflection Plots ###
    ########################
    
    plt.ioff()
    plt.clf()
    
    if len(span_disc):
        
        ### Leading Edge comparison ### magnitude
        plt.figure(14, figsize=(8, 6))
        plt.clf()
        axs = plt.axes()
        plt.title('Num. and shifted Val. Model -- LE Deflection Magnitude -- Max (Num.): %.2f mm' % np.max( np.sqrt(U_LE_Model[0,:]**2 + U_LE_Model[1,:]**2) ) )
        plt.ylabel('Displacement magnitude [mm]', fontsize=14)
        plt.xlabel('x location (spanwise) [mm]', fontsize=14)
        plt.plot(LE_xlocs, np.sqrt((U_LEs_FEM[1,:,1]+ (version != '_V2') * correction_LE)**2 + U_LEs_FEM[1,:,2]**2), '-')
        plt.plot(LE_xlocs, np.sqrt((U_LEs_FEM[0,:,1]+ (version != '_V2') * correction_LE)**2 + U_LEs_FEM[0,:,2]**2), '-.')
        plt.plot(span_disc, np.sqrt(U_LE_Model[0,:]**2 + U_LE_Model[1,:]**2), '-x')
        plt.legend(['Val. w/out loads', 'Val. full load case', 'Num. Model full load case'])
                
        plt.savefig('Plots/LC1_UM_LE_Model_shifted' + version + '.eps', format='eps')
        
        ### Trailing Edge comparison ### magnitude
        plt.figure(15, figsize=(8, 6))
        plt.clf()
        axs = plt.axes()
        plt.title('Num. and shifted Val. Model -- TE Deflection Magnitude -- Max (Num.): %.2f mm' % np.max( np.sqrt(U_TE_Model[0,:]**2 + U_TE_Model[1,:]**2) ) )
        plt.ylabel('Displacement magnitude [mm]', fontsize=14)
        plt.xlabel('x location (spanwise) [mm]', fontsize=14)
        plt.plot(TE_xlocs, np.sqrt((U_TEs_FEM[1,:,1]+ (version != '_V2') * correction_TE)**2 + U_TEs_FEM[1,:,2]**2), '-')
        plt.plot(TE_xlocs, np.sqrt((U_TEs_FEM[0,:,1]+ (version != '_V2') * correction_TE)**2 + U_TEs_FEM[0,:,2]**2), '-.')
        plt.plot(span_disc, np.sqrt(U_TE_Model[0,:]**2 + U_TE_Model[1,:]**2), '-x')
        plt.legend(['Val. w/out loads', 'Val. full load case', 'Num. Model full load case'])
                
        plt.savefig('Plots/LC1_UM_TE_Val_Model_shifted' + version + '.eps', format='eps')

        
    ### Leading Edge ###
    plt.figure(10, figsize=(8, 6))
    plt.clf()
    axs = plt.axes()
    plt.subplot(211)
    plt.title('Validation Data -- Global LE Deflection -- Maximum: %.2f mm' % np.max(U_LEs_FEM[1,:,1]))
    plt.ylabel('y-displacement [mm]')
    plt.plot(LE_xlocs, U_LEs_FEM[1,:,1], '-')
    plt.plot(LE_xlocs, U_LEs_FEM[0,:,1], '-.')
    plt.legend(['Val. w/out loads', 'Val. full load case'])
    
    plt.subplot(212)
    plt.xlabel('x location (spanwise) [mm]')
    plt.ylabel('z-displacement [mm]')
    plt.plot(LE_xlocs, U_LEs_FEM[1,:,2], '-')
    plt.plot(LE_xlocs, U_LEs_FEM[0,:,2], '-.')
    
    plt.savefig('Plots/LC1_UYZ_LE_Val' + version + '.eps', format='eps')
    
    
    ### Trailing Edge ###
    plt.figure(11, figsize=(8, 6))
    plt.clf()
    axs = plt.axes()
    plt.subplot(211)
    plt.title('Validation Data -- Global TE Deflection -- Maximum: %.2f mm' % np.max(U_TEs_FEM[1,:,1]))
    plt.ylabel('y-displacement [mm]')
    plt.plot(TE_xlocs, U_TEs_FEM[1,:,1], '-')
    plt.plot(TE_xlocs, U_TEs_FEM[0,:,1], '-.')
    plt.legend(['Val. w/out loads', 'Val. full load case'])
    
    plt.subplot(212)
    plt.xlabel('x location (spanwise) [mm]')
    plt.ylabel('z-displacement [mm]')
    plt.plot(TE_xlocs, U_TEs_FEM[1,:,2], '-')
    plt.plot(TE_xlocs, U_TEs_FEM[0,:,2], '-.')
    
    plt.savefig('Plots/LC1_UYZ_TE_Val' + version + '.eps', format='eps')
    
    
    plt.ion()
    
    

    

    
    
    
    

def getFEMSection(xloc, h_a, c_a, filename, all_nodes, rib_nodes=[]):

    nodes     = all_nodes[all_nodes[:,1].argsort(),:]
    numnodes  = len(nodes)
    
    if len(rib_nodes):
        nodes_slice = rib_nodes
    else:
        unique_x  = np.unique(nodes[:,1])
        
        nodes_slice_idx = np.argmin(abs(unique_x - xloc))
        nodes_x_loc     = unique_x[nodes_slice_idx]
        nodes_slice     = nodes[np.where(nodes[:,1] == nodes_x_loc), 0][0]
    
    ### read stresses
    line_ranges = np.array([[24, 8087], [8109, 12140], [12162, 18433], [18455, 26518]])
    diff_lines  = (np.diff(line_ranges,1,1)+1)
    cum_lines   = np.cumsum(diff_lines)
    total_lines = np.sum(diff_lines)
    
    # prealloc
    S = np.zeros((total_lines, 3))
    
    # get stresses
    S[0:cum_lines[0]]            = np.genfromtxt(filename, skip_header=line_ranges[0,0]-1, max_rows=diff_lines[0,0])[:,[1,2,3]]
    S[cum_lines[0]:cum_lines[1]] = np.genfromtxt(filename, skip_header=line_ranges[1,0]-1, max_rows=diff_lines[1,0])[:,[1,2,3]]
    S[cum_lines[1]:cum_lines[2]] = np.genfromtxt(filename, skip_header=line_ranges[2,0]-1, max_rows=diff_lines[2,0])[:,[1,2,3]]
    S[cum_lines[2]:]             = np.genfromtxt(filename, skip_header=line_ranges[3,0]-1, max_rows=diff_lines[3,0])[:,[1,2,3]]
    S                            = S[S[:,0].argsort(),:]
    
    
    ##########################
    ### Post proc stresses ###
    ##########################
    
    S_post    = np.zeros((numnodes, 2))
    S_post[:,0]    = range(1, 1+numnodes)
    
    for i in range(1, 1+numnodes):
        S_post[i-1,1]    = np.mean(S   [np.where(S[:,0] == i), 1:][0])*1e3
        
    
    ### assign to ribs ###
    
    arc_coords = np.zeros(len(nodes_slice))
    
    # sort ribs
    nodes_slice_tmp = all_nodes[nodes_slice.astype('int')-1]
    num             = len(nodes_slice_tmp[:,0])
    
    cutoff = 1e-12

    left = nodes_slice_tmp[:,3] > cutoff*np.ones((num))
    right = nodes_slice_tmp[:,3] < -cutoff*np.ones((num))
    top = nodes_slice_tmp[:,2] > cutoff*np.ones((num))
    bottom = nodes_slice_tmp[:,2] < -cutoff*np.ones((num))
    in_spar=  abs(nodes_slice_tmp[:,3]) < 1e-12*np.ones((num))

    left         = nodes_slice_tmp[left]
    left         = np.flipud(left[left[:,2].argsort(),:])
    right_bottom = nodes_slice_tmp[right * bottom]
    right_bottom = right_bottom[right_bottom[:,2].argsort(),:]
    right_top    = nodes_slice_tmp[right * top]
    right_top    = right_top[right_top[:,2].argsort(),:]
    spar         = nodes_slice_tmp[in_spar]
    spar         = np.flipud(spar[spar[:,2].argsort(),:])

    nodes_slice_sort = np.zeros(num)
    nodes_amounts = [len(left), len(right_bottom), len(right_top), len(spar)]
    cum_nodes     = np.cumsum(nodes_amounts)    
    
    nodes_slice_sort[0           :cum_nodes[0]] = left[:,0]
    nodes_slice_sort[cum_nodes[0]:cum_nodes[1]] = right_bottom[:,0]
    nodes_slice_sort[cum_nodes[1]:cum_nodes[2]] = right_top[:,0]
    nodes_slice_sort[cum_nodes[2]:cum_nodes[3]] = spar[:,0]
    nodes_slice_sort = nodes_slice_sort.astype('int')
        
    j = 0
    for node in nodes_slice_sort:
        if j < len(left):
            # circular section
            arc_coords[j] = h_a/2 * np.arctan2(nodes[node-1, 3], nodes[node-1, 2])
        elif j < len(left) + len(right_bottom):
            arc_coords[j] = np.pi * h_a/2 + np.linalg.norm(nodes[node-1, 2:] - np.array([-h_a/2, 0]))
        elif j < len(left) + len(right_bottom) + len(right_top):
            arc_coords[j] = np.pi * h_a/2 + np.linalg.norm(np.array([h_a/2, c_a-h_a/2]))\
                                            + np.linalg.norm(nodes[node-1, 2:] - np.array([0, -c_a+h_a/2]))
        else:
            arc_coords[j] = np.pi * h_a/2 + np.linalg.norm(np.array([h_a/2, c_a-h_a/2]))*2\
                                            - nodes[node-1, 2] + h_a/2
        
        j = j + 1
        
    
        
    S_post_slice = S_post[nodes_slice_sort.astype('int')-1, 1]


    return arc_coords, S_post_slice, all_nodes[nodes_slice_sort-1]



def plotFEMSection(nodes, stresses, title, filename):
    
    plt.ioff()
    
    # scatters
    plt.figure(0, figsize=(7.5, 4.5))
    plt.clf()
    
    axs = plt.axes()
    plt.scatter(nodes[:,3], nodes[:,2], c=stresses, cmap='jet')
    plt.title(title + '-- Maximum: %.2f MPa' % np.max(stresses))
    plt.axis('equal')
    plt.xlabel('z location [mm]')
    plt.ylabel('y location [mm]')
    axs.invert_xaxis()
    plt.tight_layout
    cbar = plt.colorbar()
    plt.clim(0,100)
    cbar.set_label('von Mises stress [MPa]', rotation=90)
    plt.savefig('Plots/'+filename+'.eps', format='eps')
    
    plt.ion()



