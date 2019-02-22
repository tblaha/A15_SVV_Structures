import numpy as np
import numpy.linalg as lin
import UniversalConstants as UC
import matplotlib.pyplot as plt

def shearFlowRibActuator(P, h_a=UC.h_a, c_a=UC.c_a, theta=UC.theta):
	'''
	INPUTS:
	- P:
	The force from the actuator acting on the rib.
	
	- h_a:
	The thickness of the aileron.
	This variable is a given constant of the simulation.
	
	- c_a:
	The chordlength of the aileron.
	This variable is a given constant of the simulation.
	
	- theta:
	The maximum deflection the aileron is at. A positive angle
	corresponds with a pitch down deflection.
	This variable is a given constant of the simulation.
	
	OUTPUTS:
	- The shear flow on the upper half of the front (the curved part) of the rib (positive going upwards).
	- The shear flow on the upper (straight) side of the rib (positive going from the spar the the TE).
	- The shear flow on the lower (straight) side of the rib (positive going from the TE to the spar).
	- The shear flow on the lower half of the front (the curved part) of the rib (positive going upwards).
	- The shear flow in the web of the nose (the D-section bit) (positive going from the bottom to the top).
	- The shear flow in the web of the tail (the triangle bit) (positive going from the top to the bottom).
	'''
	
	an2 = ((h_a**2)/8.)*((np.pi/2.) - 1.)
	at2 = ((((np.pi/2.) + 1.)*((h_a**2)/8.)) + ((c_a*h_a)/4.))
	aa = ((c_a*h_a)/2.) - ((h_a**2)/4.)

	A = np.matrix([
	[h_a/2., -h_a/2., -h_a/2., h_a/2.],
	[-h_a/2., (-c_a + (h_a/2.)), (c_a - (h_a/2.)), h_a/2.],
	[-2.*at2, 0., 0., -2.*at2],
	#[-an2, -at2, -at2, -an2]
	[-np.pi*((h_a**2)/4.), -2.*aa, 0., -2.*an2]
	])

	#b = np.array([-P*np.sin(theta), -P*np.cos(theta), ((P*np.sin(theta)*c_a) - (P*np.cos(theta)*(h_a/2.))), -P*np.cos(theta)*(h_a/2.)])
	b = np.array([-P*np.sin(theta), -P*np.cos(theta), ((P*np.sin(theta)*c_a) - (P*np.cos(theta)*(h_a/2.))), (P*np.sin(theta)*(h_a/2.)-P*np.cos(theta)*h_a)])

	q_rib = lin.solve(A, b)
	
	q_1 = (q_rib[0] + q_rib[3])*h_a
	q_2 = (q_rib[1] + q_rib[2])*h_a
	
	return q_rib[0], q_rib[1], q_rib[2], q_rib[3], q_1, q_2

'''
# This is some stuff I used for testing.
P_list = np.linspace(0., 1200., 10)
q_41 = []
q_12 = []
q_23 = []
q_34 = []
for P in P_list:
	x = solve(P)
	q_41.append(x[0])
	q_12.append(x[1])
	q_23.append(x[2])
	q_34.append(x[3])

plt.plot(P_list, q_41, label='q_41')
plt.plot(P_list, q_12, label='q_12')
plt.plot(P_list, q_23, label='q_23')
plt.plot(P_list, q_34, label='q_34')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
'''