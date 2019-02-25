# -*- coding: utf-8 -*-
"""
Author: tblaha & dverkooij
Date  : 2019-02-18
"""


from UniversalConstants import *
from Stiffeners import *
import numpy as np


def discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_c, z_c, booms_between, cg_correction):
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
    # y_c                 : y-component of centroid [mm] (float)
    # z_c                 : z-component of centroid [mm] (float) MEASURED FROM HINGE LINE
    # booms_between       : The amount of booms in between stiffeners; 
    #                       stiffeners themselves are automatically booms (int)
    #
    # --- OUTPUTS --- #
    # 2d numpy array:
    # | y-loc | z-loc | area if y-bending | area if z-bending | cell id |
    # | 0     | 0     | 1                 | 2                 | 1       |
    # | ...
    #
    # y and z locations are from the centroid of the section
    # cell id: 1 (exclusively left cell, counter clockwise sorted)
    #          2 (exclusively right cell, counter clockwise sorted)
    #          3 (exclusively spar, downwards sorted)
    
    
    # ----- General setup and preallocation ----- #
    # just some simple stuff
    
    # to achieve a more uniform boom distribution, more booms between the 2 
    # ends of the spars are needed. This is a factor for this upscaling
    spar_upscaling = 4
    
    # in total there will be n_st stiffeners, so prealloc that
    S = np.zeros((n_st, 5))
    
    # for booms, that is more complex:
    # n_st +                         # one boom at every stiffener
    # booms_between*(n_st+1) +       # in each of the (n_st+1) segments there are booms_between booms
    # booms_between*spar_upscaling + # upscaling for the spar
    # 2                              # two additional booms at the ends of the spar
    B = np.zeros((n_st + booms_between*(n_st+spar_upscaling), 5)) # works better without the +2
    
    
    
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
    length_per_stiff_seg = total_length/(len(S)-0.5)
    
    # length per boom segment (here, the booms in the spar need to be
    # subtracted since we want to know the length intervals in the skin, not
    # the spar as the spar is handled later)
    length_per_boom_seg  = length_per_stiff_seg/(1+booms_between) # works better without the -2
    
    # number of stiffeners and booms in the circular segment
    stiffs_quarter_circular = np.floor(sc_arc_length/2/length_per_stiff_seg)
    booms_quarter_circular  = np.floor(sc_arc_length/2/length_per_boom_seg)

    
    
    # ----- booms in circular section ----- #
    # iterate over the amount of booms (CCW) in the circular section (using the
    # angle that the lines connecting the hinge line and the booms make) and
    # compute their area by taking skin contributions and adding the stiffener
    # area where there is a stiffener    
    
    # going counter clockwise from the first boom in the circular sections,
    # how many lonely booms are there until we hit the first stiffener
    # NOTE: the +1 is needed because every repetitive unit of stiffeners and
    # in-between booms is (booms_between+1)
    booms_to_first_stiff = (booms_quarter_circular)%(booms_between+1)
    
    # iterate over the booms in the circular section
    for i in range(int(booms_quarter_circular)*2+1): # +1 because there is one on the z-axis
        
        # the radial distance of each boom in the circular section is constant,
        # so only the angle needs to be calculated: 0 angle means on the z-axis
        # and positive angle means below the z-axis
        angle = (booms_quarter_circular - i) * length_per_boom_seg/(2*sc_arc_length) * 2*np.pi
#        print(angle)
        
        # using the angle, get the location using the radial distance h_a/2
        B[i,0]     = np.sin(angle)*h_a/2
        B[i,1]     = np.cos(angle)*h_a/2
        
        # all the booms computed in this for-loop are in beam section 1
        B[i,4]     = 1
        
        # add the skin contributions of the skin segments in-between the booms
        # treated in this section (the "outside" contribution to the booms at
        # the very end and the very beginning of this section will be added
        # later when fixing corner cases)
        # one skin segment distributes to two booms, i and i-1
        if i: # if not the first boom in this for-loop
            if abs(B[i,1]-z_c) > 1e-6: # quick check if not infinite
                # stress ratio reduces to length ratio from neutral line because
                # we assume pure bending with linear variation
                B[i,2]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            if abs(B[i-1,1]-z_c) > 1e-6:
                B[i-1,2] += t_sk/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            if abs(B[i,0]-y_c) > 1e-6:
                B[i,3]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            if abs(B[i-1,0]-y_c) > 1e-6:
                B[i-1,3] += t_sk/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        # Add stiffener area, if we are encoutering a stiffener (if the modulo
        # returns 0)
        # booms_to_first_stiff is the offset to the first stiffener when going
        # CCW
        
        angle_stiff = - np.pi/2 - angle
        # centroid location
        u_vec = np.array([np.cos(angle_stiff), np.sin(angle_stiff)])
        actual_centroid  = B[i,0:2] + u_vec * Ybar_st
        
        if not (i-booms_to_first_stiff)%(booms_between+1): 
            if abs(B[i,1]-z_c)>1e-6 and cg_correction:
                B[i,2] += A_st * ((actual_centroid[1]-z_c) / (B[i,1]-z_c))**2
            else:
                B[i,2] += A_st
                
            if abs(B[i,0]-y_c)>1e-6 and cg_correction:
                B[i,3] += A_st * ((actual_centroid[0]-y_c) / (B[i,0]-y_c))**2
            else:
                B[i,3] += A_st
        
        # Fix corner cases
        if i == 0: # if first boom
            # (np.pi/2 - angle) * h_a/2 is the arc length from the first boom
            # to the top end of the spar
            B[i,2]  += t_sk/6 * (np.pi/2 - angle) * h_a/2 * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * (np.pi/2 - angle) * h_a/2 * (2 + (h_a/2-y_c)/(B[i,0]-y_c))
            
        if i == int(booms_quarter_circular)*2+1-1: # if last boom
            # (np.pi/2 + angle) * h_a/2 is the arc length from the last boom
            # to the top end of the spar
            B[i,2]  += t_sk/6 * (np.pi/2 + angle) * h_a/2 * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * (np.pi/2 + angle) * h_a/2 * (2 + (-h_a/2-y_c)/(B[i,0]-y_c))

    
    
    # ----- booms in straight sections ----- #
    # compute the boom locations and areas in the same general way as above 
    # but now for the bottom straight segement. Then, basically reverse the
    # and mirror the locations to the top straight segment.
    
    # compute the length in the straight segment for when the first boom
    # appears (straight_sec_start)
    leftover_arc_length = sc_arc_length/2 - angle*h_a/2 # arc length still in circular segment
    straight_sec_start  = length_per_boom_seg-leftover_arc_length%length_per_boom_seg
        
    # stiffeners and booms in either of the two straight segments
    stiffs_half_straight    = np.floor((straight_length/2-straight_sec_start)/length_per_stiff_seg)
    booms_half_straight     = np.floor((straight_length/2-straight_sec_start)/length_per_boom_seg)
        
    # iterate again
    for j in range(int(booms_half_straight)):
        
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
        B[i,0:2]   = np.transpose(bottom_pnt + unit_vec * (straight_sec_start + j * length_per_boom_seg))
        
        # we are in section 2
        B[i,4]     = 2
        
        # skin contributions (exactly like above)
        if j:
            B[i,2]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c) / (B[i,1]-z_c))
            B[i-1,2] += t_sk/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)   / (B[i-1,1]-z_c))
            B[i,3]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c) / (B[i,0]-y_c))
            B[i-1,3] += t_sk/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)   / (B[i-1,0]-y_c))
        
        # add the stiffener area where there is a stiffener
        angle_stiff = np.arctan2(h_a/2 , c_a-h_a/2)
        u_vec = np.array([np.cos(angle_stiff), np.sin(angle_stiff)])
        actual_centroid = B[i,0:2] + u_vec * Ybar_st
        if not (i-booms_to_first_stiff)%(booms_between+1):
            if abs(B[i,1]-z_c)>1e-6 and cg_correction:
                B[i,2]   += A_st * ((actual_centroid[1]-z_c) / (B[i,1]-z_c))**2
            else:
                B[i,2]   += A_st
    
            if abs(B[i,0]-y_c)>1e-6 and cg_correction:
                B[i,3]   += A_st * ((actual_centroid[0]-y_c) / (B[i,0]-y_c))**2
            else:
                B[i,3]   += A_st
                
        # Fix corner cases, but only for the first one
        # AM I SURE THAT THERE IS NO CORNER CASE AT THE END OF THIS SECTION
        if j == 0:
            B[i,2]  += t_sk/6 * straight_sec_start * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * straight_sec_start * (2 + (-h_a/2-y_c)/(B[i,0]-y_c))
            
            
    # second (top) straight segment by mirroring the booms
    k = i # index in the B array to call the booms computed for the bottom
    for j in range(int(booms_half_straight)):
        i = i + 1
        
        # mirroring about the z-axis
        B[i,0:2] = B[k, 0:2] * np.array([[-1, 1]])
        
        # still section 2
        B[i,4]   = 2
        
        # count down the index to move to the next boom of the bottom
        k = k - 1
        
        # skin contributions (exactly like above)
        if j:
            B[i,2]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            B[i-1,2] += t_sk/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            B[i,3]   += t_sk/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            B[i-1,3] += t_sk/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        # add the stiffener area where there is a stiffener
        angle_stiff = np.arctan2(h_a/2 , -c_a+h_a/2)
        u_vec = np.array([np.cos(angle_stiff), np.sin(angle_stiff)])
        actual_centroid = B[i,0:2] + u_vec * Ybar_st
        if not (i-booms_to_first_stiff)%(booms_between+1):
            if abs(B[i,1]-z_c)>1e-6 and cg_correction:
                B[i,2]   += A_st * ((actual_centroid[1]-z_c) / (B[i,1]-z_c))**2
            else:
                B[i,2]   += A_st
    
            if abs(B[i,0]-y_c)>1e-6 and cg_correction:
                B[i,3]   += A_st * ((actual_centroid[0]-y_c) / (B[i,0]-y_c))**2
            else:
                B[i,3]   += A_st
            
        # Fix corner cases, but only for the last one
        # AM I SURE THAT THERE IS NO CORNER CASE AT THE START OF THIS SECTION         
        if j == int(booms_half_straight)-1:
            B[i,2]  += t_sk/6 * straight_sec_start * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]  += t_sk/6 * straight_sec_start * (2 + (h_a/2-y_c)/(B[i,0]-y_c))
        
        
        
    # ----- booms in spar ----- #
    for l in range(booms_between*spar_upscaling+2): # the two comes from the top and bottom ends
        i = i + 1
        
        # walk down from the top (h_a/2) to the bottom (-h_a+h_a/2)
        B[i, 0:2] = np.array([ -l * h_a / (booms_between*spar_upscaling+1) + h_a/2, 0] )
        
        # we call the spar section 3
        B[i,4]    = 3
        
        # just like above, skin contributions
        if l:
            B[i,2]   += t_sp/6 * length_per_boom_seg * (2 + (B[i-1,1]-z_c)/(B[i,1]-z_c))
            B[i-1,2] += t_sp/6 * length_per_boom_seg * (2 + (B[i,1]-z_c)  /(B[i-1,1]-z_c))
            B[i,3]   += t_sp/6 * length_per_boom_seg * (2 + (B[i-1,0]-y_c)/(B[i,0]-y_c))
            B[i-1,3] += t_sp/6 * length_per_boom_seg * (2 + (B[i,0]-y_c)  /(B[i-1,0]-y_c))
        
        # no stiffeners in here
        
        # top corner case        
        if l == 0:
            B[i,2]   += t_sp/6 * length_per_boom_seg * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]   += t_sp/6 * length_per_boom_seg * (2 + (h_a/2-y_c)/(B[i,0]-y_c))
          
        # bottom corner case
        if l == booms_between*spar_upscaling+2-1:
            B[i,2]   += t_sp/6 * length_per_boom_seg * (2 + (0-z_c)/(B[i,1]-z_c))
            B[i,3]   += t_sp/6 * length_per_boom_seg * (2 + (-h_a/2-y_c)/(B[i,0]-y_c))
        
    
    # shitty postfix
    emtpy_lines = int(np.floor(len(B[np.where(B[:,3:5] == 0)])/2))
    B = np.delete(B, [np.arange(len(B)-emtpy_lines,len(B))],0)
        
    # bring to centroidal coordinate system
    B[:,0:2] = B[:,0:2] - np.array([y_c, z_c])
    
    # finally, return the booms
    return  B
    


 
def plotCrossSection(B):
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
    else:
        axs[0].scatter(B[:,1], B[:,0])
        axs[1].scatter(B[:,1], B[:,0])
        
    
    # format: axis equal and invert the z axis (x-axis in the plot referece frame)
    axs[0].axis('equal')
    axs[1].axis('equal')
    axs[0].invert_xaxis()
    axs[1].invert_xaxis()
    
    # make pretty
    fig.tight_layout()
    
    # show
    plt.show()
      
    
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

#Verification spanwise discretization
    
#span_disc=discretizeSpan(x_h1, x_h2, x_h3, d_a, l_a, nodes_between=50,ec=0.0001,offset=30)
#for i in range(len(span_disc)-1):
#    if span_disc[i]>span_disc[i+1]:
#        print('ERROR: Value smaller than previous value, less not increaing linearly')
    



# debugging

#B=discretizeCrossSection(h_a, c_a, n_st, 1, t_sk, t_sp, 0, -98, 3)
#for i in range(4,3,-1):
     # = generateStiffeners(h_a, c_a, n_st, t_st*(w_st+h_st-t_st), t_sk, t_sp)
#     B=discretizeCrossSection(254,1398, n_st, t_st*(w_st+h_st-t_st), t_sk, t_sp, 0, -98, i)
     #plotCrossSection(B)

#cross_disc=discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_bar, z_bar, 27)

#print(cross_disc)
     
B = discretizeCrossSection(h_a, c_a, n_st, t_st*(w_st+h_st-t_st), t_sk, t_sp, 0, -98, 5, 0)

     
     