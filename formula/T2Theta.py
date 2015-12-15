import math

####
#	author: Perry Lee
#	mail:	voldemort92205@gmail.com
#	date:	2015/12/15
####

# parameters
Rd = 287.0
Cp = 1004.0
T0 = 273.15		# T[k] = T[degree C] + 273.15
P0 = 1000		# reference pressure [hPa]

def Tc2Theta (T, P):
	# T [degree C], P [hPa]
	Theta = (T+T0)* 1.0 * math.pow (1.0*P0/P, Rd/Cp)
	return Theta

def Tk2Theta (T, P):
	# T [k], P [hPa]
	Theta = T * 1.0 * math.pow (1.0*P0/P, Rd/Cp)
	return Theta
