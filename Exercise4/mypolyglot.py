from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)
		
square(bob, 25)
square(bob, 50)
square(bob, 100)
square(bob, 150)
square(bob, 200)
square(bob, 250)
	
wait_for_user()