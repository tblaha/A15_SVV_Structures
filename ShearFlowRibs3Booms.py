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
	- The shear flow on the front (the curved part) of the rib (positive going upwards).
	- The shear flow on the upper (straight) side of the rib (positive going from the spar the the TE).
	- The shear flow on the lower (straight) side of the rib (positive going from the TE to the spar).
	- The shear flow in the web of the nose (the D-section bit) (positive going from the bottom to the top).
	- The shear flow in the web of the tail (the triangle bit) (positive going from the top to the bottom).
	'''

	A = np.matrix([
	[h_a, -h_a/2., -h_a/2.],
	[0., (-c_a + h_a/2.), (c_a - h_a/2.)],
	[-np.pi*h_a/4., 0., -((2.*c_a) - (h_a))]
	])

	b = np.array([-P*np.sin(theta), -P*np.cos(theta), P*np.sin(theta)])

	q_rib = lin.solve(A, b)
	
	q_1 = q_rib[0]*h_a
	q_2 = (q_rib[1] + q_rib[2])*(h_a/2.)
	
	return q_rib[0], q_rib[1], q_rib[2], q_1, q_2

#print(shearFlowRibActuator(1200.))

'''
# This is some stuff I used for testing.
P_list = np.linspace(0., 1200., 10)
q_n = []
q_u = []
q_l = []
for P in P_list:
	x = solve(P)
	q_n.append(x[0])
	q_u.append(x[1])
	q_l.append(x[2])

plt.plot(P_list, q_n, label='q_n')
plt.plot(P_list, q_u, label='q_u')
plt.plot(P_list, q_l, label='q_l')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
'''