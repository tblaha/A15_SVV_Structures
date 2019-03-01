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

class shearFlowRib:
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
	
	OUTPUTS:
	Initializes the matrix A with the geometrical data that can then be
	used to calculate the shear flows.
	'''
	
	def __init__(self, B, Z_bar, Y_bar):
		plot_q_sections = True
		self.plot_q_sections = plot_q_sections
		plot_cross_section = False
		plot_cross_section_live = False
		plot_matrix = False
		print_statements = False
		self.print_statements = print_statements
		
		if print_statements:
			print('There are %i points in the cross-section discretization.' % len(B))

		### This thing produces the array of point coordinates of the points on the circumfarence of the rib.###
		# Define the point types.
		nose = 1
		tail = 2
		spar = 3
		self.nose = nose
		self.tail = tail
		self.spar = spar
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
		self.points = points
		points_spar = np.array(points_spar)
		self.points_spar = points_spar
		'''
		points_spar_transpose = points_spar.transpose()
		plt.plot(points_spar_transpose[0], points_spar_transpose[1], 'bo')
		plt.grid()
		plt.title('Spar points')
		plt.tight_layout()
		plt.show()
		'''
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
		self.A = np.zeros((dim, dim))
		self.A = np.matrix(self.A)
		
		for row in range(len(points)):
			for col in range(len(points)-1):
				area = areaTriangle(points[row], points[col], points[col + 1]) + two_point_areas[col]
				self.A[row, col] = -2. * area
			col = len(points)-1
			area = areaTriangle(points[row], points[len(points)-1], points[0]) + two_point_areas[len(points)-1]
			self.A[row, len(points)-1] = -2. * area
		
		points_spar_index = 1
		for row in range(len(points), len(self.A)-1):
			for col in range(len(points)-1):
				area = areaTriangle(points_spar[points_spar_index], points[col], points[col + 1]) + two_point_areas[col]
				self.A[row, col] = -2. * area
			col = len(points)-1
			area = areaTriangle(points_spar[points_spar_index], points[len(points)-1], points[0]) + two_point_areas[len(points)-1]
			self.A[row, len(points)-1] = -2. * area
			points_spar_index += 1
		
		for row in range(len(points)):
			points_spar_index = 0
			for col in range(len(points), len(self.A)):
				if points[row][2] == nose:
					area = areaTriangle(points[row], points_spar[points_spar_index], points_spar[points_spar_index + 1])
					self.A[row, col] = 2. * area
				elif points[row][2] == tail:
					area = areaTriangle(points[row], points_spar[points_spar_index], points_spar[points_spar_index + 1])
					self.A[row, col] = -2. * area
				else: self.A[row, col] = 0.
				points_spar_index += 1
		
		for i in range(len(points)-1):
			self.A[len(self.A)-1, i] = points[i+1][1] - points[i][1]
		self.A[len(self.A)-1, len(points)-1] = points[0][1] - points[len(points)-1][1]
		
		points_spar_index = 0
		for i in range(len(points), len(self.A)):
			self.A[len(self.A)-1, i] = points_spar[points_spar_index+1][1] - points_spar[points_spar_index][1]
			points_spar_index += 1
		
		eigen_values = eigvals(self.A)
		condition_number = max(eigen_values)/min(eigen_values)
		
		if print_statements:
			print(max(eigen_values))
			print(min(eigen_values))
			print('The eigenvalue of the matrix A is %f.' % condition_number)
		
		if plot_matrix:
			plt.imshow(self.A,interpolation='none')
			plt.colorbar()
			plt.show()
		### END ###
	
	#def solve(P_1=0., P_2=0., F_z=0., F_y=0.):
	def calculateShear(self, P_1, P_2, F_z, F_y):
		'''
		INPUTS:
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
		
		nose = self.nose
		tail = self.tail
		spar = self.spar
		dim = len(self.A)
		points = self.points
		points_spar = self.points_spar
        
		### This bit creates the b vector. The b vector is dependend on the load case. ###
		b = np.zeros(dim)
		for i in range(len(points)):
			b[i] += (points[i][1] - (h_a/2.))*P_1*np.cos(theta_radians) + ((h_a/2.) - points[i][0])*P_1*np.sin(theta_radians)
			b[i] += ((h_a/2.) - points[i][1])*P_2*np.cos(theta_radians) + (points[i][0] - (h_a/2.))*P_2*np.sin(theta_radians)
			b[i] += (-0. + points[i][1])*F_z + (0. - points[i][0])*F_y
		
		points_spar_index = 1
		for i in range(len(points), len(self.A)-1):
			b[i] += (points_spar[points_spar_index][1] - (h_a/2.))*P_1*np.cos(theta_radians) + ((h_a/2.) - points_spar[points_spar_index][0])*P_1*np.sin(theta_radians)
			b[i] += ((h_a/2.) - points_spar[points_spar_index][1])*P_2*np.cos(theta_radians) + (points_spar[points_spar_index][0] - (h_a/2.))*P_2*np.sin(theta_radians)
			b[i] += (-0. + points_spar[points_spar_index][1])*F_z + (0. - points_spar[points_spar_index][0])*F_y
			points_spar_index += 1
		
		b[len(self.A)-1] = F_y + (P_1 - P_2)*np.sin(theta_radians)
		
		### END ###
		
		if self.print_statements:
			print('The determinant of A: det(A) = %i.' % det(self.A))
		
		q = lstsq(self.A, b, rcond=1e-10)
		q = q[0]
		
		if self.plot_q_sections:
			plt.title('Number of points: ' + str(len(points)))
			plt.plot(range(len(self.A)), q, color='lightgray')
			for i in range(len(self.A)):
				plt.plot(i, q[i], 'bo')
			plt.tight_layout()
			plt.grid()
			plt.show()
		
		### Here we check whether the sum of the shear forces matches the applied forces. ###
		fz = 0.
		fy = 0.
		for i in range(len(points)-1):
			fz += q[i]*(points[i+1][0] - points[i][0])
			fy += q[i]*(points[i+1][1] - points[i][1])
		fz += q[len(points)-1]*(points[0][0] - points[len(points)-1][0])
		fy += q[len(points)-1]*(points[0][1] - points[len(points)-1][1])
		for i in range(len(points_spar)-1):
			fy += q[len(points) + i]*(points_spar[i+1][1] - points_spar[i][1])
		
		F_z_tot = F_z + (P_1 - P_2)*np.cos(theta_radians)
		F_y_tot = F_y + (P_1 - P_2)*np.sin(theta_radians)
		
		if fz != F_z_tot or fy != F_y_tot:
			print('A discrepancy was found!')
			print('The sum of the forces in the z direction was: %f' % F_z_tot)
			print('The sum of the calculated shear flows in the z direction was: %f' % fz)
			print('The sum of the forces in the y direction was: %f' % F_y_tot)
			print('The sum of the calculated shear flows in the y direction was: %f' % fy)
		
		if self.print_statements:
			print('The sum of the shearforces in the z direction: fz = %f.' % F_z_tot)
			print('The sum of the shearforces in the y direction: fy = %f.' % F_y_tot)
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

def plotRibShear(cross_disc, z_bar, q_Rib, arc_coords, vonMises_before, vonMises_after, ribname):
	
	plt.ioff()
    
	rib_arc = np.zeros(len(q_Rib)-1)
	D_coord = (np.arctan2(cross_disc[1,1]+z_bar,cross_disc[1,0]) - np.arctan2(cross_disc[0,1]+z_bar,cross_disc[0,0])) * h_a/2
	first_spar = sum(cross_disc[:,4] != 3)
	D_spar  = cross_disc[first_spar,0] - cross_disc[first_spar+1,0]
	j = 0
	k = 0
	for i in range(len(q_Rib)-1):
		if cross_disc[i,4] == 1:
			rib_arc[i] = i * D_coord
		elif cross_disc[i,4] == 2:
			rib_arc[i] = np.pi * h_a/2 + j * D_coord
			j += 1
		else:
			rib_arc[i] = np.pi * h_a/2 + 2*np.sqrt( (h_a/2)**2 + (c_a - h_a/2)**2 )\
                         + k * D_spar
			k += 1
    
	fig = plt.figure(2001)
	plt.clf()
	plt.title('Rib ' + ribname + ' shear plotted over perimeter')
	plt.xlabel('Tangential coordinate along Aileron [mm]', fontsize=14)
	plt.ylabel('Shear flow [N/mm] and Shear stress [MPa]', fontsize=14)
	plt.plot(rib_arc, q_Rib[0:-1], '-x')
	plt.plot(arc_coords, -(vonMises_after - vonMises_before) / sqrt(3), '-o')
	plt.tight_layout()
	plt.grid()
	plt.legend(['Numerical Model (Flow)', 'Validation Data (Stress)'])
	plt.savefig('Plots/Ribs/Rib' + ribname + '.eps', format='eps')
	
	plt.ion()