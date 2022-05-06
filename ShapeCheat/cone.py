import math
import time

def cone_info(radius, height):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR V = pi x radius^2 x (height/3)
	volume = ((math.pi * (radius**2))*height)/3
	# FORMULA FOR SA = (pi x radius) x (radius + (sqrt((height^2) + (radius^2))))
	surface_area = (math.pi * radius) * (radius + (math.sqrt((height**2) + (radius**2))))
	# FORMULA FOR LSA = (pi x radius) x (sqrt((height^2) + (radius^2)))
	lateral_surface = (math.pi * radius) * (math.sqrt((height**2) + (radius**2)))
	# FORMULA FOR SH = sqrt((radius^2) + (height^2))
	slant_height = math.sqrt((radius**2) + (height**2))
	# FORMULA FOR BASE = pi X radius^2
	base = math.pi * (radius**2)

	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\nDiameter = {radius * 2}\nLateral Surface Area = {lateral_surface}\nSlant Height = {slant_height}\nBase Area = {base}\n\nHEIGHT = {height}\nRADIUS = {radius}"

	return information

r = float(input("Type radius: "))
h = float(input("Type height: "))

print(cone_info(r,h))

time.sleep(60)