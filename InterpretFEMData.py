# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:30:26 2019

@author: Till
"""

from UniversalConstants import *
import numpy as np
import matplotlib.pyplot as plt


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

header_lines_S = 19

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
S_up_L_post_ribA = S_up_L_post[nodes_ribA, 1]
S_up_L_post_ribB = S_up_L_post[nodes_ribB, 1]
S_up_L_post_ribC = S_up_L_post[nodes_ribC, 1]
S_up_L_post_ribD = S_up_L_post[nodes_ribD, 1]

S_up_nL_post_ribA = S_up_nL_post[nodes_ribA, 1]
S_up_nL_post_ribB = S_up_nL_post[nodes_ribB, 1]
S_up_nL_post_ribC = S_up_nL_post[nodes_ribC, 1]
S_up_nL_post_ribD = S_up_nL_post[nodes_ribD, 1]

S_down_L_post_ribA = S_down_L_post[nodes_ribA, 1]
S_down_L_post_ribB = S_down_L_post[nodes_ribB, 1]
S_down_L_post_ribC = S_down_L_post[nodes_ribC, 1]
S_down_L_post_ribD = S_down_L_post[nodes_ribD, 1]

S_down_nL_post_ribA = S_down_nL_post[nodes_ribA, 1]
S_down_nL_post_ribB = S_down_nL_post[nodes_ribB, 1]
S_down_nL_post_ribC = S_down_nL_post[nodes_ribC, 1]
S_down_nL_post_ribD = S_down_nL_post[nodes_ribD, 1]



#######################
### von Mises plots ###
#######################

plt.figure(0)
axs = plt.axes()
plt.scatter(nodes[nodes_ribA,3], nodes[nodes_ribA,2], c=S_up_L_post_ribA, cmap='jet')
plt.title('Rib A: Maximum von Mises: %.2f MPa' % np.max(S_up_L_post_ribA))
plt.axis('equal')
axs.invert_xaxis()
plt.tight_layout
plt.colorbar()
plt.savefig('FEMData/LC1_RibA_scatter.eps', format='eps')

plt.figure(1)
axs = plt.axes()
plt.scatter(nodes[nodes_ribB,3], nodes[nodes_ribB,2], c=S_up_L_post_ribB, cmap='jet')
plt.title('Rib B: Maximum von Mises: %.2f MPa' % np.max(S_up_L_post_ribB))
plt.axis('equal')
axs.invert_xaxis()
plt.tight_layout
plt.colorbar()
plt.savefig('FEMData/LC1_RibB_scatter.eps', format='eps')

plt.figure(2)
axs = plt.axes()
plt.scatter(nodes[nodes_ribC,3], nodes[nodes_ribC,2], c=S_up_L_post_ribC, cmap='jet')
plt.title('Rib C: Maximum von Mises: %.2f MPa' % np.max(S_up_L_post_ribC))
plt.axis('equal')
axs.invert_xaxis()
plt.tight_layout
plt.colorbar()
plt.savefig('FEMData/LC1_RibC_scatter.eps', format='eps')

plt.figure(3)
axs = plt.axes()
plt.scatter(nodes[nodes_ribD,3], nodes[nodes_ribD,2], c=S_up_L_post_ribD, cmap='jet')
plt.title('Rib D: Maximum von Mises: %.2f MPa' % np.max(S_up_L_post_ribD))
plt.axis('equal')
axs.invert_xaxis()
plt.tight_layout
plt.colorbar()
plt.savefig('FEMData/LC1_RibD_scatter.eps', format='eps')



########################
### Deflection Plots ###
########################

#TE_xlocs = nodes_TE[:,1]
#U_up_L_TE  = U_up_L [nodes_TE[:,0].astype('int'), :][:,[1,2,3]]
#U_up_nL_TE = U_up_nL[nodes_TE[:,0].astype('int'), :][:,[1,2,3]]
#
#U_down_L_TE  = U_down_L [nodes_TE[:,0].astype('int'), :][:,[1,2,3]]
#U_down_nL_TE = U_down_nL[nodes_TE[:,0].astype('int'), :][:,[1,2,3]]
#
#plt.subplot(221)
#plt.plot(TE_xlocs, U_up_nL_TE[:,1])
#plt.plot(TE_xlocs, U_up_L_TE[:,1])
#
#plt.subplot(223)
#plt.plot(TE_xlocs, U_up_nL_TE[:,2])
#plt.plot(TE_xlocs, U_up_L_TE[:,2])
#
#plt.subplot(222)
#plt.plot(TE_xlocs, U_down_nL_TE[:,1])
#plt.plot(TE_xlocs, U_down_L_TE[:,1])
#
#plt.subplot(224)
#plt.plot(TE_xlocs, U_down_nL_TE[:,2])
#plt.plot(TE_xlocs, U_down_L_TE[:,2])



























