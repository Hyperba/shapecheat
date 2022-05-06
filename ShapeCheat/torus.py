import math
import time

def torus_info(major_radius, minor_radius):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR V = (pi x minor_radius ^2) x (2 x pi x major_radius)
	volume = (math.pi * (minor_radius**2)) * (2 * math.pi * major_radius)
	# FORMULA FOR SA = (2 x pi x major_radius) x (2 x pi x minor_radius)
	surface_area = (2 * math.pi * major_radius) * (2 * math.pi * minor_radius)

	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\n\nMINOR RADIUS = {minor_radius}\nMAJOR RADIUS = {major_radius}"

	return information

R = float(input("Type major radius: "))
r = float(input("Type minor radius: "))

if R < r:
	print("That does not work. Major radius must be bigger")
else:	
	print(torus_info(r,R))

time.sleep(60)