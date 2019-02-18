import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def shapeOfAileron(x_coords, displ_na, d_theta, theta, x_2, x_a, h_a, c_a, plot=False):
	'''
	INPUTS:
	- x_coords:
	This is an array holding the x values of the different cross-sections,
	given in the order that they are ordered on the aileron,
	starting from the part closest to the fuselage (positive x-direction).
	
	- displ_na:
	The input for the displacements will be an array consisting of two arrays.
	The first array holds the displacements in the y-direction, the second array
	the displacements in the z-direction. The arrays are ordered in the same
	manner as the x_coords array.
	
	- d_theta:
	The rate of twist for each section given in an array. The array is ordered
	in the order that the sections are on the aileron, starting from the part
	closest the the fuselage (positive x-direction).
	
	- theta:
	The angle the aileron was given to be at. The position of this twist is
	assumed to be at actuator I as this actuator is given to be fixed (jammed).
	The cross-section at which this angle holds will be referred to as the
	fixed section.
	This variable is a given constant of the simulation.
	
	- x_2:
	The distance between the side of the aileron closest to the fuselage and
	hinge 2.
	This variable is a given constant of the simulation.
	
	- x_a:
	The distance between the two actuators.
	This variable is a given constant of the simulation.
	
	- h_a:
	The thickness of the airfoil.
	This variable is a given constant of the simulation.
	
	- c_a:
	The chord length of the airfoil.
	This variable is a given constant of the simulation.
	
	- plot:
	This variable will dictate whether a plot will be made or not.
	If the variable is True, a plot will be made with the TE, LE and NA.
	The chords will also be plotted at each position that the aileron
	was cut (and the tips).
	
	METHOD:
	Note that the spanwise points at which we'll be avaluating the aileron will be referred to
	as the cross-sections. The parts inbetween the cross-sections will be referred to as the
	sections.
	First, using the x_coords data, we will calculate the width of each section.
	Using the d_theta data we can then calculate how much each cross-section has twisted.
	To do this, we will assume that the side of the aileron closest to the fuselage is fixed
	and all the consecutive cross-sections are twisted relative to this cross-section. The
	advantage of doing this is that the coordinate system is the same for each cross-section
	and the d_theta data has the correct sign. We will then save the twist angle at each cross-section.
	Now as some part of the aileron is given to be at a certain angle, we need to adjust these
	angles (add a constant to all calculated angles like we are twisting the entire aileron) such that
	that part, lets call it the 'fixed cross-section', is indeed at that given angle.
	To do this, we will first find the section that this fixed cross-section is in. Then we will calculate
	the twist of this cross-section by making an extra cut there and determining how much it
	has twisted compared with the cross-section besides it. This is done by using the d_theta data
	corresponding to that section and the distance between the fixed cross-section and
	the cross-section besides it. The difference between the angle we wanted and the angle we
	have is then added to the twist angle at each cross-section.
	Now we can simply calculate the position of the LE and TE relative to the NA by using basic
	trigonometry and add this to the displacement values of the NA to get the displacement of the
	LE and TE. We then return the maximum (absolute) displacement of the LE and TE in the y
	direction and the x coordinate of the corresponding cross-sections.
	
	OUTPUTS:
	- The maximum (absolute) displacement of the ailerons LE.
	- The maximum (absolute) displacement of the ailerons TE.
	- The x coordinate of the cross-section at which the displacement of the LE is maximum (absolute).
	- The x coordinate of the cross-section at which the displacement of the TE is maximum (absolute).
	'''
	
	# We start by calculating the width of the spanwise section we divide the aileron in.
	# These widths will be stored in section_widths.
	# There will be one less section
	section_widths = np.zeros(len(x_coords)-1)
	for i in range(len(x_coords)-1):
		section_width = x_coords[i+1] - x_coords[i]
		section_widths[i] = section_width
	
	# Using the rate of twist of the sections I'll calculate the angle that each section is at.
	# I'll do this assuming that the first section (the one closest to the fuselage) is not rotated.
	# Once I have this, I'll add/subtract a constant angle to correct for this assumption.
	section_thetas = np.zeros(len(x_coords))
	for i in range(len(x_coords)-1):
		section_theta = section_thetas[i] + section_widths[i]*d_theta[i]
		section_thetas[i+1] = section_theta
	
	# Now I need to now what constant angle I need to add/subtract from the previously calculated
	# angles. To obtain this, I look at what angle the cross-section is at that I assumed did not
	# twist. I compare it with the angle that I had previously calculated and the difference is the
	# constant angle.
	fixed_section_x_coord = x_2 - (x_a/2.)
	dist_section_fixed_section = x_coords - fixed_section_x_coord
	fixed_section_found = False
	search_index = len(x_coords) - 1
	while not fixed_section_found:
		if dist_section_fixed_section[search_index] <= 0:
			fixed_section_found = True
			fixed_section_index = search_index
		search_index -= 1
	correction_angle = theta - section_thetas[fixed_section_index] + (fixed_section_x_coord - x_coords[fixed_section_index])*d_theta[fixed_section_index]
	
	# Now we correct the angles we previously calculated by adding the correction.
	section_thetas = section_thetas + correction_angle
	
	LE_y_coords = displ_na[0] - np.sin(section_thetas)*(h_a/2.)
	LE_z_coords = displ_na[1] + np.cos(section_thetas)*(h_a/2.)
	LE_coords = np.array([LE_y_coords, LE_z_coords])
	
	TE_y_coords = displ_na[0] + np.sin(section_thetas)*(c_a - (h_a/2.))
	TE_z_coords = displ_na[1] - np.cos(section_thetas)*(c_a - (h_a/2.))
	TE_coords = np.array([TE_y_coords, TE_z_coords])
	
	# Here I plot the NA, LE and TE if so desired (if plot is set to True).
	if plot == True:
		# Make the figure and create a 3D axes object.
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d', aspect='equal')
		
		# To make the aileron be oriented correctly in the plot, we need to
		# pass the coordinates in the order x, z, y as opposed to x, y, z.
		# The axis will be labelled to match the axis system we used.
		ax.plot(x_coords, displ_na[1], displ_na[0], color='blue', label='NA')			# This bit will plot the NA.
		ax.plot(x_coords, te_coords[1], le_coords[0], color='red', label='LE')		# This bit will plot the LE.
		ax.plot(x_coords, te_coords[1], te_coords[0], color='green', label='TE')	# This bit will plot the TE.
		
		# At each cross-section, I will draw the chord line (which is just a line from
		# the LE to the TE).
		for i in range(len(x_coords)):
			ax.plot([x_coords[i], x_coords[i]], [le_coords[1, i], te_coords[1, i]], [le_coords[0, i], te_coords[0, i]], color='lightgray')
		
		# Now add the axis labels to match the system we've used.
		ax.set_xlabel('x')
		ax.set_ylabel('z')
		ax.set_zlabel('y')
		
		# Include the legend.
		plt.legend()
		
		# Make it all a bit tighter.
		plt.tight_layout()
		
		# And show our glorious plot.
		plt.show()
	
	#The maximum displacement is found by simply taking the maximum of all the y
	# displacements of the LE/TE. Note that we need to add the abs key to the max()
	# function to have it take the absolute maximum.
	disp_le_y_max = max(le_coords[0], key=abs)
	disp_te_y_max = max(te_coords[0], key=abs)
	
	# Now the corresponding x coordinate. We find this by looking at the index
	# that the disp_le_y_max and disp_te_y_max variables have in there cooresponding
	# arrays. As there is no function to get there index for arrays, we first convert them
	# into lists.
	disp_le_max_x_index = list(le_coords[0]).index(disp_le_y_max)
	disp_te_max_x_index = list(te_coords[0]).index(disp_te_y_max)
	
	# The index is then used to get the x coordinates.
	disp_le_max_x = x_coords[disp_le_max_x_index]
	disp_te_max_x = x_coords[disp_te_max_x_index]
	
	# Now we return the maximum displacement of the LE and TE in the y direction and the
	# x coordinates of the corresponding cross-sections.
	return disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x

def shapeOfAileronTest():
	'''
	This function is just to test the shapeOfAileron() function above.
	It takes no inputs as the inputs with which we are going to test
	the shapeOfAileron() function will be defined below.
	We then output the variables that the shapeOfAileron() function outputs.
	'''
	
	# Here we define the variables which we want to pass to the shapeOfAileron() funcion.
	x_coords = np.array([0., 100., 200., 300., 400., 500.])
	displ_na = np.array([[0., 1., 2., 3., 4., 5.], [0., 3., 6., 9., 12., 15.]])
	#displ_na = np.array([[0., 0., 0., 0., 0., 0.], [0., 0., 0., 0., 0., 0.]])
	d_theta = np.array([-1, -0.5, -0.2, 0.3, 1.2])*0.001
	#d_theta = np.zeros(5)
	theta = 26.*(np.pi/180.)
	x_2 = 250.
	x_a = 10.

	h_a = 12.5
	c_a = 50.
	
	# And here we run the shapeOfAileron() function and print its outputs.
	disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x = shapeOfAileron(x_coords, displ_na, d_theta, theta, x_2, x_a, h_a, c_a, plot=True)
	print disp_le_y_max
	print disp_te_y_max
	print disp_le_max_x
	print disp_te_max_x