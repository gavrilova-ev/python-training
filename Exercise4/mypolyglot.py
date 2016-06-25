from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

def do_n_times(f, func_param, n):
	for i in range(n):
		f(func_param)
	
def draw_and_turn(length):
	fd(bob,length)
	lt(bob)

do_n_times(draw_and_turn, 100, 4)	
	
wait_for_user()