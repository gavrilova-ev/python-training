from math import pi

def volume(r): 
	return 4./3 * pi * r**3
print volume(5)

def price(quantity):
	return quantity * 2495 * 0.4 + 300 + 75 * (quantity - 1)
print price(60)/100

def timetoint(h,m,s):
	return 3600*h + 60*m + s
	
def inttotime(number):
	s = number % 60
	number /= 60
	m = number % 60
	h = number / 60
	return (h,m,s)


h,m,s =  inttotime(timetoint(6,52,0) + 2 * timetoint(0,8,15) + 3 * timetoint(0, 7,12))

print "{hours:02}:{mins:02}:{secs:02}".format(hours=h, mins=m, secs=s)
	