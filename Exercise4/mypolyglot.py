from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)
		
def polygon(t, length, n):
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)
		
polygon(bob, 50, 6)
	
wait_for_user()