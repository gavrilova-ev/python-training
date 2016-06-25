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
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)
		
def circle(t, r):
	circumference = 2 * pi * r
	polygon(t, circumference/100, 100)
	
circle(bob, 20)
circle(bob, 50)
circle(bob, 100)
			
wait_for_user()