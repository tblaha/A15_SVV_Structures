import numpy as np
from numpy.linalg import solve, lstsq, inv, eigvals, det
from UniversalConstants import *
import matplotlib.pyplot as plt

def areaTriangle(point_1, point_2, point_3):
	A_x = point_1[0]
	A_y = point_1[1]
	B_x = point_2[0]
	B_y = point_2[1]
	C_x = point_3[0]
	C_y = point_3[1]
	return np.abs(((A_x * (B_y - C_y)) + (B_x * (C_y - A_y)) + (C_x * (A_y - B_y)))/2.)

def shearFlowRib(B, Z_bar, Y_bar, P_1=0., P_2=0., F_z=0., F_y=0.):
	'''
	INPUTS:
	- B:
	The boom discretization of the cross-section produced by the
	discretizeCrossSection() function in the discretization.py module.
	
	- Z_bar:
	The z coordinate of the centroid of the idealized cross-section as
	measured from the hingeline.
	
	- Y_bar:
	The y coordinate of the centroid of the idealized cross-section as
	measured from the hingeline.
	
	- P_1:
	The force of actuator I.
	
	- P_2:
	The force of actuator II.
	
	- F_z:
	The force in the positive z direction of the hinge.
	
	- F_y:
	The force in the positive y direction of the hinge.
	
	OUTPUTS:
	- The shearflows on the perimeter of the rib given in an array.
	Each entry corresponds with a section of the boom discretization,
	only considering the sections on the perimeter. The sections are
	ordered starting from the top of the spar, going down over the nose.
	The shear flows are also defined positive in this direction.
	- The shearflow in the web of the nose of the aileron.
	Defined positive counter-clockwise.
	- The shearflow in the web of the back of the aileron.
	Defined positive counter-clockwise.
	'''
	
	plot_q_sections = True
	plot_cross_section = True
	plot_cross_section_live = False
	plot_matrix = True
	print_statements = True
    
	if print_statements:
		print('There are %i points in the cross-section discretization.' % len(B))

	### This thing produces the array of point coordinates of the points on the circumfarence of the rib.###
	# Define the point types.
	nose = 1
	tail = 2
	spar = 3
	'''
	points = []
	points.append([0., h_a/2., spar)
	current_type = nose
	for y, z, dump1, dump2, type in B:
		if type != current_type and type == tail:
			points.append([0., -h_a/2., spar)
		points.append([z+ Z_bar, y + Y_bar, type])
	'''
	###
	points = []
	points_spar = []
	points.append([0., h_a/2., spar])
	for point in B:
		if point[4] == nose: points.append([point[1] + Z_bar, point[0] + Y_bar, nose])
	points.append([0., -h_a/2., spar])
	for point in B:
		if point[4] == tail: points.append([point[1] + Z_bar, point[0] + Y_bar, tail])
	for point in B:
		if point[4] == spar:
			points_spar.append([point[1] + Z_bar, point[0] + Y_bar, spar])
	###
	points = np.array(points)
	points_spar = np.array(points_spar)
	
	points_spar_transpose = points_spar.transpose()
	plt.plot(points_spar_transpose[0], points_spar_transpose[1], 'bo')
	plt.grid()
	plt.title('Spar points')
	plt.tight_layout()
	plt.show()
	
	if plot_cross_section:
		plt.plot(points.transpose()[0], points.transpose()[1], 'bo')
		B = np.array(B)
		plt.plot(B[:, 1], B[:, 0], 'r+')
		plt.grid()
		plt.tight_layout()
		plt.show()
	if print_statements:
		print('There are %i points on the circumference.' % len(points))
	### END ###

	### Here we construct the matrix A. This matrix is only dependend on the geometry of the cross-section (the boom positions of the booms in this case). ###
	points_transpose = points.transpose()
	sparcap_top = points_transpose[1].argmax()
	sparcap_bot = points_transpose[1].argmin()

	two_point_areas = np.zeros(len(points))
	for i in range(sparcap_bot):
		angle_1 = np.arctan2(points[i][1], points[i][0])
		angle_2 = np.arctan2(points[i+1][1], points[i+1][0])
		angle = np.abs(angle_1 - angle_2)
		area_circle = (np.pi * (h_a**2))/4.
		area_pie = (angle/(2. * np.pi)) * area_circle
		area_triangle = areaTriangle([0., 0.], points[i], points[i+1])
		area_moon = area_pie - area_triangle
		two_point_areas[i] = area_moon
	
	bottom_tail = points_transpose[0].argmin()
	
	area_tail_triangle = np.abs(points[bottom_tail][1])*((c_a - (h_a/2.)) - np.abs(points[bottom_tail][0]))
	
	two_point_areas[bottom_tail] = area_tail_triangle
	
	if plot_cross_section_live:
		plt.ion()
		plt.grid()
		plt.tight_layout()
		for y, z, dump1, dump2, type in B:
			if type == spar: plt.plot(z, y, 'ro')
			elif type == nose: plt.plot(z, y, 'bo')
			elif type == tail: plt.plot(z, y, 'go')
			else:
				print(y, z, dump1, dump2, type)
				print('Type not recognized!')
			plt.show()
			plt.pause(0.05)
		plt.ioff()
		plt.show()
	
	dim = len(points) + len(points_spar) - 1
	A = np.zeros((dim, dim))
	A = np.matrix(A)
	
	for row in range(len(points)):
		for col in range(len(points)-1):
			area = areaTriangle(points[row], points[col], points[col + 1]) + two_point_areas[col]
			A[row, col] = -2. * area
		col = len(points)-1
		area = areaTriangle(points[row], points[len(points)-1], points[0]) + two_point_areas[len(points)-1]
		A[row, len(points)-1] = -2. * area
	
	points_spar_index = 1
	for row in range(len(points), len(A)-1):
		for col in range(len(points)-1):
			area = areaTriangle(points_spar[points_spar_index], points[col], points[col + 1]) + two_point_areas[col]
			A[row, col] = -2. * area
		col = len(points)-1
		area = areaTriangle(points_spar[points_spar_index], points[len(points)-1], points[0]) + two_point_areas[len(points)-1]
		A[row, len(points)-1] = -2. * area
		points_spar_index += 1
	
	for row in range(len(points)):
		points_spar_index = 0
		for col in range(len(points), len(A)):
			if points[row][2] == nose:
				area = areaTriangle(points[row], points_spar[points_spar_index], points_spar[points_spar_index + 1])
				A[row, col] = 2. * area
			elif points[row][2] == tail:
				area = areaTriangle(points[row], points_spar[points_spar_index], points_spar[points_spar_index + 1])
				A[row, col] = -2. * area
			else: A[row, col] = 0.
			points_spar_index += 1
	
	for i in range(len(points)-1):
		A[len(A)-1, i] = points[i+1][1] - points[i][1]
	A[len(A)-1, len(points)-1] = points[0][1] - points[len(points)-1][1]
	
	points_spar_index = 0
	for i in range(len(points), len(A)):
		A[len(A)-1, i] = points_spar[points_spar_index+1][1] - points_spar[points_spar_index][1]
		points_spar_index += 1
	
	eigen_values = eigvals(A)
	condition_number = max(eigen_values)/min(eigen_values)
	
	if print_statements:
		print(max(eigen_values))
		print(min(eigen_values))
		print('The eigenvalue of the matrix A is %f.' % condition_number)
	
	if plot_matrix:
		plt.imshow(A,interpolation='none')
		plt.colorbar()
		plt.show()
	### END ###

	### This bit creates the b vector. The b vector is dependend on the load case. ###
	b = np.zeros(dim)
	for i in range(len(points)):
		b[i] += (points[i][1] - (h_a/2.))*P_1*np.cos(theta_radians) + ((h_a/2.) - points[i][0])*P_1*np.sin(theta_radians)
		b[i] += ((h_a/2.) - points[i][1])*P_2*np.cos(theta_radians) + (points[i][0] - (h_a/2.))*P_2*np.sin(theta_radians)
		b[i] += (-0. + points[i][1])*F_z + (0. - points[i][0])*F_y
	
	points_spar_index = 1
	for i in range(len(points), len(A)-1):
		b[i] += (points_spar[points_spar_index][1] - (h_a/2.))*P_1*np.cos(theta_radians) + ((h_a/2.) - points_spar[points_spar_index][0])*P_1*np.sin(theta_radians)
		b[i] += ((h_a/2.) - points_spar[points_spar_index][1])*P_2*np.cos(theta_radians) + (points_spar[points_spar_index][0] - (h_a/2.))*P_2*np.sin(theta_radians)
		b[i] += (-0. + points_spar[points_spar_index][1])*F_z + (0. - points_spar[points_spar_index][0])*F_y
		points_spar_index += 1
	
	b[len(A)-1] = F_y + (P_1 - P_2)*np.sin(theta_radians)
	
	### END ###
	
	if print_statements:
		print('The determinant of A: det(A) = %i.' % det(A))
	
	q = lstsq(A, b, rcond=1e-10)
	q = q[0]
	
	if plot_q_sections:
		plt.title('Number of points: ' + str(len(points)))
		plt.plot(range(len(A)), q, color='lightgray')
		for i in range(len(A)):
			plt.plot(i, q[i], 'bo')
		plt.tight_layout()
		plt.grid()
		plt.show()
	
	### Here we check whether the sum of the shear forces matches the applied forces. ###
	fz = 0
	fy = 0
	for i in range(len(points)-1):
		fz += q[i]*(points[i+1][0] - points[i][0])
		fy += q[i]*(points[i+1][1] - points[i][1])
	fz += q[len(points)-1]*(points[0][0] - points[len(points)-1][0])
	fy += q[len(points)-1]*(points[0][1] - points[len(points)-1][1])
	if print_statements:
		print('The sum of the shearforces in the z direction: fz = %f.' % fz)
		print('The sum of the shearforces in the y direction: fy = %f.' % fy)
	### END ###
	
	### Determine the shearflows in the ribs. ###
	q_1 = 0
	q_2 = 0
	for i in range(len(points)-1):
		if points[i][2] == nose or points[i+1][2] == nose:
			q_1 += q[i]*(points[i+1][1] - points[i][1])
		if points[i][2] == tail or points[i+1][2] == tail:
			q_2 += q[i]*(points[i][1] - points[i+1][1])
	q_2 += q[len(points)-1]*(points[len(points)-1][1] - points[0][1])
	q_1 = q_1/h_a
	q_2 = q_2/h_a
	### END ###
	
	return q, q_1, q_2

# This bit was used for testing.
import Stiffeners as s
import Centroid as C
import DiscretizationV2 as d
import discretization as d
q_1_list = []
q_2_list = []
q_list = []
S_uncor = s.generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 0)
S_cor = s.generateStiffeners(h_a, c_a, n_st, A_st, t_sk, t_sp, Ybar_st, 1)
cg_cor_stiffeners=1
if cg_cor_stiffeners==1:
    Stiffeners=S_cor
else:
    Stiffeners=S_uncor
y_c, z_c = C.findCentroid(Stiffeners)
booms_between_list = [0, 1, 5, 10, 20, 30, 40, 50]
booms_between_list = range(0, 55, 5)
booms_between_list = [0, 1, 5, 10, 20]
#booms_between_list = [0, 1, 2, 5, 10, 20, 50, 100]
#booms_between_list = range(200, 201)
#booms_between_list = [0]
n_st = 3
for i in booms_between_list:
	booms_between = i
	#B = d.discretizeCrossSection(S_cor, S_uncor, h_a, c_a, n_st, A_st, t_sk, t_sp, y_c, z_c, booms_between, Ybar_st, cg_cor_stiffeners)
	B = d.discretizeCrossSection(h_a, c_a, n_st, A_st, t_sk, t_sp, y_c, z_c, booms_between, Ybar_st, 0.)
	for line in B: print(line)
	q, q_1, q_2 = shearFlowRib(B, z_c, y_c, F_z=19390./2., F_y=8397./2., P_1=100.)
	q_1_list.append(q_1)
	q_2_list.append(q_2)
	q_list.append(q)
	print('The calculated shearflow in the nose web: q_1 = %f.' % q_1)
	print('The calculated shearflow in the tail web: q_2 = %f.' % q_2)
	print()
plt.plot(booms_between_list, q_1_list, 'b-o', label='q_1')
plt.plot(booms_between_list, q_2_list, 'g-o', label='q_2')
plt.grid()
plt.tight_layout()
plt.show()