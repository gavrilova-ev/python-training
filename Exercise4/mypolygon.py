from swampy.TurtleWorld import *
from math import *

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)
		
def polygon(t, length, n):
	angle = 360.0/n
	polyline(t,length,n,angle)
		
def circle(t, r):
	arc(t,r,360)

def arc(t, r, angle):
	arc_length = 2 * pi * r * angle / 360
	n = int(arc_length/3) +1
	step_length = arc_length/n
	step_angle = float(angle) / n
	polyline(t,step_length,n,step_angle)
		
def polyline(t,length,n,angle):
	for i in range(n):
		fd(t,length)
		lt(t,angle)
		

arc(bob,20,180)

wait_for_user()