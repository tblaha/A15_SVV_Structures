import numpy as np;/
import matplotlib.pyplot as plt
import UniversalConstants as UC
from mpl_toolkits.mplot3d import Axes3D

def shapeOfAileron(x_coords, displ_na, d_theta, theta, Z_bar, h_a=UC.h_a, c_a=UC.c_a, plot=False):
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
	closest the the fuselage (positive x-direction).  Note that angles are taken
	positive counter clockwise.
	
	- theta:
	The angle of the maximum upward deflection of the aileron.
	This variable is a given constant of the simulation.
	
	- Z_bar:
	The z coordinate of the centroid of the cross-section as measured from the
	hingeline.
	
	- d_a:
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
	As the maximum deflection of the aileron was given, we need to correct the twist angles (think of
	it as rotating the entire aileron) such that the maximum calculated angle matches the given angle.
	The difference between the angle we wanted and the angle we have is then added to the twist
	angle at each cross-section. Now we can simply calculate the position of the LE and TE relative
	to the NA by using basic trigonometry and add this to the displacement values of the NA to get
	the displacement of the LE and TE. We then return the maximum (absolute) displacement of the
	LE and TE in the y direction and the x coordinate of the corresponding cross-sections.
	
	OUTPUTS:
	- The maximum (absolute) displacement of the ailerons LE.
	- The maximum (absolute) displacement of the ailerons TE.
	- The x coordinate of the cross-section at which the displacement of the LE is maximum (absolute).
	- The x coordinate of the cross-section at which the displacement of the TE is maximum (absolute).
	'''
	
	# We start by calculating the width of the spanwise sections we divide the aileron in.
	# These widths will be stored in section_widths.
	# There will be one less section as there are cross-sections thus when initializing
	# the section_widths array we need to make it one shorter then the amount of
	# cross-sections we have (the amount of cross-sections we have is the same as
	# the size of the x_coords array as the x_coords array holds all the x coordinates
	# of the cross-sections). This array will be initialized as an array of all zeros.
	section_widths = np.zeros(len(x_coords)-1)
	
	# When looking in the positive x direction, the cross-section with index i is followed
	# by the section with index i which in turn is followed by cross-section i+1.
	# So the width of the ith section is the diference between the x coordinate of
	# the i+1th cross-section and the x coordinate of the ith cross-section.
	# As the last cross-section isn't followed by a section (we have reached the end of
	# the aileron), we don't need to calculate the length of the section
	for i in range(len(section_widths)):
		# We calculate the section width.
		section_width = x_coords[i+1] - x_coords[i]
		
		#Then we update the corresponding entry of the section_widths array.
		section_widths[i] = section_width
	
	# Using the rate of twist of the sections I'll calculate the angle that each cross-section is at.
	# I'll do this assuming that the first cross-section (the one closest to the fuselage and index 0)
	# is not rotated. The angles that the cross-sections are at will then be stored in the
	# section_thetas array. This array will be initialized as an array of all zeros.
	section_thetas = np.zeros(len(x_coords))
	
	# The angle which the i+1th cross-section is at
	# is equal to the sum of the angle that the ith cross-section is at and the amount
	# that the ith section has twisted.
	# As the first angle is taken to be 0, we can determine the consecutive angles
	# by going over the sections.
	for i in range(len(section_widths)):
		# We calculate the angle the cross-section is at.
		section_theta = section_thetas[i] + section_widths[i]*d_theta[i]
		
		# And then we update its corresponding entry in section_thetas.
		# Note that we never update the 0th entry as the first angle is taken
		# to be 0 and the array was initialized to be all zeros.
		section_thetas[i+1] = section_theta
	
	# Now we need to know the maximum upward deflection (largest positive angle)
	# that we currently have. This angle can then be used to determine how much we
	# still need to rotate the aileron such that the maximum upward deflection angle
	# matches the given one. Note that we want the maximum angle, and not maximum
	# absolute angle, as the given deflection angle is the maximum upward deflection angle.
	theta_max = max(section_thetas)
	
	# The correction_angle is than the difference between the maximum angle we want
	# and the maximum angle we actually have.
	correction_angle = theta - theta_max
	
	# Now we correct the angles we previously calculated by adding the correction.
	section_thetas = section_thetas + correction_angle
	
	# For the displacements of the LE and TE we use the displacement of the NA and
	# add/subtract the displacement of the LE/TE with respect to the NA. For this, we'll also assume that
	# the displacement of the hinge line is the same as the displacement of the NA.
	# As the angles are taken with respect to the positive z axis, the displacements in the
	# z direction are calculated with the cos of the angles times the distance between the
	# LE/TE and the NA. The sin is used for the displacements in the y direction.
	# The distance between the hinge line and the LE is half the height of the airfoil.
	# For a positive angle the LE of the aileron goes down in the y direction. Thus, the
	# displacement of the LE in the y direction needs to be subtracted from the displacement
	# of the NA in the y direction.
	le_y_coords = displ_na[0] - np.sin(section_thetas)*((h_a/2.)-Z_bar)
	
	# As the LE is in fron of the hinge line, the displacement of the LE with respect to the hinge line
	# in the z direction should be added to the displacement of the NA in the z direction.
	le_z_coords = displ_na[1] + np.cos(section_thetas)*(h_a/2.-Z_bar)
	
	# The y and z coordinates are then put together in an array.
	le_coords = np.array([le_y_coords, le_z_coords])
	
	# The distance between the hinge line and the TE is the chord length minus the distance
	# between the LE and hinge line.
	# The TE will go up in the y direction for a positive angle so we need to add the displacement
	# in the y direction.
	te_y_coords = displ_na[0] + np.sin(section_thetas)*(c_a - (h_a/2.) + Z_bar)
	
	# As the TE is behind the hinge line, the displacement of the TE with respect to the hinge line
	# in the z direction should be subtracted from the displacement of the NA in the z direction.
	te_z_coords = displ_na[1] - np.cos(section_thetas)*(c_a - (h_a/2.) + Z_bar)
	
	# The y and z coordinates are then put together in an array.
	te_coords = np.array([te_y_coords, te_z_coords])
	
	# Here I plot the NA, LE and TE if so desired (if plot is set to True).
	if plot == True:
		# Make the figure and create a 3D axes object.
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		
		# To make the aileron be oriented correctly in the plot, we need to
		# pass the coordinates in the order x, z, y as opposed to x, y, z.
		# The axis will be labelled to match the axis system we used.
		ax.plot(x_coords, displ_na[1], displ_na[0], color='blue', label='NA')			# This bit will plot the NA.
		ax.plot(x_coords, le_coords[1], le_coords[0], color='red', label='LE')			# This bit will plot the LE.
		ax.plot(x_coords, te_coords[1], te_coords[0], color='green', label='TE')		# This bit will plot the TE.
		
		# At each cross-section, I will draw the chord line (which is just a line from
		# the LE to the TE).
		for i in range(len(x_coords)):
			ax.plot([x_coords[i], x_coords[i]], [le_coords[1, i], te_coords[1, i]], [le_coords[0, i], te_coords[0, i]], color='lightgray')
		
		# Now add the axis labels to match the system we've used.
		ax.set_xlabel('x')
		ax.set_ylabel('z')
		ax.set_zlabel('y')
		
		# The next 8 lines of code are basically straight from stackoverflow.
		# They are needed to set scale of the axis right, i.e., such that circles
		# are plotted as circles and not ovals.
		
		#First we look what the current plot limits are. These will be set automatically
		# based on the data.
		limits = np.array([ax.get_xlim3d(), ax.get_ylim3d(), ax.get_zlim3d()])
		
		# As matplotlib automatically centres on the plotted data, the centre of the
		# data is at the centre of the current plot. Thus, to get the centre of the plot
		# we look at the means of the limits for each axis.
		plot_centre_x = np.mean(limits[0])
		plot_centre_y = np.mean(limits[1])
		plot_centre_z = np.mean(limits[2])
		
		# Now to get the amount the plot needs to include around the origin,
		# we'll look at the length of the axis that was originally plotted.
		# Half of the axis that was the longest will be then be added around
		# each centre point.
		radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
		
		# The new axis limits can then be set.
		ax.set_xlim3d([plot_centre_x - radius, plot_centre_x + radius])
		ax.set_ylim3d([plot_centre_y - radius, plot_centre_y + radius])
		ax.set_zlim3d([plot_centre_z - radius, plot_centre_z + radius])
		
		# This bit is then needed to make the axis appear equal size in the plot.
		ax.set_aspect('equal')
		
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
	x_coords = np.array([0., 100., 200., 300., 400., 500.])*10.
	displ_na = np.array([[0., 1., 2., 3., 4., 5.], [0., 3., 6., 9., 12., 15.]])
	displ_na = np.array([[0., 0., 0., 0., 0., 0.], [0., 0., 0., 0., 0., 0.]])
	d_theta = np.array([-1, -0.5, -0.2, 0.3, 1.2])*0.0001
	#d_theta = np.ones(5)*0.0005
	#d_theta = np.zeros(5)
	theta = 26.*(np.pi/180.)
	Z_bar = -100.
	#h_a = 12.5
	#c_a = 50.
	
	# And here we run the shapeOfAileron() function and print its outputs.
	#disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x = shapeOfAileron(x_coords, displ_na, d_theta, theta, x_h2, d_a, h_a, c_a, plot=True)
	disp_le_y_max, disp_te_y_max, disp_le_max_x, disp_te_max_x = shapeOfAileron(x_coords, displ_na, d_theta, theta, Z_bar, plot=True)
	print(disp_le_y_max)
	print(disp_te_y_max)
	print(disp_le_max_x)
	print(disp_te_max_x)
shapeOfAileronTest()