import math
import time

def tetrahedron_info(edge):
	# Code will tell us Volume and Surface Area

	# FORMULA FOR SA = sqrt(3) x edge^2
	surface_area = math.sqrt(3) * (edge**2)
	# FROMULA FOR V = edge^3 / 6 x sqrt(2)
	volume = (edge**3)/((6 * (math.sqrt(2))))
	# FORMULA FOR FA = (edge^2((sqrt(3)))/(4))
	face_area = ((edge**2)*((math.sqrt(3)))/(4))


	information = f"\nVolume = {volume}\nSurface Area = {surface_area}\nFace Area = {face_area}\n\nEDGE = {edge}"

	return information

s = float(input("Type side: "))

print(tetrahedron_info(s))

time.sleep(60)