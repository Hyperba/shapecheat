import math
import time

def cuboid_info(length, width, height):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR V = lenght x width x height
	volume = length * width * height
	# FROMULA FOR SA = 2 x ((width x length) + (height x length) + (height x width)))
	surface_area = 2 * ((width * length) + (height * length) + (height * width))
	# FORMULA FOR SD = srt(3) * side
	space_diagonal = math.sqrt(((length**2) + (width**2) + (height**2)))


	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\nSpace Diagonal = {space_diagonal}\n\nLENGTH = {length}\nWIDTH = {width}\nHEIGHT = {height}"

	return information

l = float(input("Type length: "))
w = float(input("Type width: "))
h = float(input("Type height: "))


print(cuboid_info(l, w, h))

time.sleep(60)