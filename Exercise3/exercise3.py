def right_justify(s):
	return (70 - len(s)) * ' ' + s

print right_justify('sykablyad')


def do_twice(f,value):
	f(value)
	f(value)
	
def print_spam(value):
	print value
	
def print_twice(value):
	print value+value
	
do_twice(print_twice,'spam')

def do_four(f,value):
	do_twice(f,value)
	do_twice(f,value)
	
do_four(print_spam,'bla')
do_four(print_twice,'bla')


def print_row(char1,char2, n):
	print n*(char1 + char2*4) + char1

def print_row1(n):
	print_row('+','-',n)

def print_row2(n):
	print_row('|',' ',n)
		
def print_block(num):
	print_row1(num)
	do_four(print_row2,num)
	
def print_grid(num):
	do_four(print_block,num)
	print_row1(num)
	
print_grid(4)
	