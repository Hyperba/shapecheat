import math
import time

def cube_info(side):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR V = side^3
	volume = side**3
	# FROMULA FOR SA = 6 x side^2
	surface_area = 6 * (side**2)
	# FORMULA FOR SD = srt(3) * side
	space_diagonal = math.sqrt(3) * side


	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\nSpace Diagonal = {space_diagonal}\n\nSIDE = {side}"

	return information

s = float(input("Type side: "))

print(cube_info(s))

time.sleep(60)