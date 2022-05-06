import math
import time

def cylinder_info(radius, height):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR V = pi x radius^2 x height
	volume = (math.pi * (radius**2)) * height
	# FORMULA FOR SA = 2 x pi x radius x (height + radius)
	surface_area = (math.pi * 2 * radius) * (height + radius)
	# FORMULA FOR LSA = 2 x pi x radius x height
	lateral_surface = (2 * radius * math.pi * height)
	# FORMULA FOR BASE = pi X radius^2
	base = math.pi * (radius**2)

	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\nDiameter = {radius * 2}\nLateral Surface Area = {lateral_surface}\nBase Area = {base}\n\nHEIGHT = {height}\nRADIUS = {radius}"

	return information

r = float(input("Type radius: "))
h = float(input("Type height: "))

print(cylinder_info(r,h))

time.sleep(60)