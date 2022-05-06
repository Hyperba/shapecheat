import math
import time

def sphere_info(radius):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR V = 4/3 x pi x radius^3
	volume = ((math.pi * (radius**3)) *4) / 3
	# FORMULA FOR SA = 4 x pi x radius^2
	surface_area = 4 * math.pi *(radius**2)

	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\nDiameter = {radius * 2}\n\nRADIUS = {radius}"

	return information

r = float(input("Type radius: "))

print(sphere_info(r))

time.sleep(60)