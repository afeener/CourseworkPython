# Alex Feener: py_p1.py
import sys
import random
import math

ndarts = int(sys.argv[1])
in_circ = 0

for i in range(ndarts):
	x = random.random()
	y = random.random()
	distance = math.sqrt(x*x + y*y)
	if  distance <= 1.0:
		in_circ+= 1
		
estimate = 4*(in_circ / ndarts)

print("pi estimate =", estimate)