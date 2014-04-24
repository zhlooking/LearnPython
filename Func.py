import math


def abs(x):
	if x < 0:
		return -x
	else:
		return x

# This is a function that do nothing:
# pass is like todo in Java, without pass there would an error
def non():
	pass

# abs(x) more compatible
def abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x < 0:
		return -x
	else:
		return x

def move(x, y, step, angle=0):
	nx = x + step*math.cos(angle)
	my = y - step*math.sin(angle)
	return nx, ny    				
# Note that the return dose not return multiple value but a tuple data struct like (nx, ny)
# If there is no return syntax in a function, the function return None by default

def power(x, n = 2):
	s = 1
	while n > 0:
		n -= 1
		s *= n;
	return s 
# To be fixed:
# draw_circle(0, 0, 20, linecolor=0xffff00, fillcolor=0xff00ff, penwidth=5)
# The above line will raise a NameError called: name 'draw_circle' is not defined

def add_append(L[]):
	return L.append('END')
# This will cause error when no paramater is passed to the function
# Use the below instead:
def add_append(L = None):
	if L is None:
		return L = []
	else:
		return L.append('END')
	

# The function that can change the number of paramaters
# The function chage the paramaters into set or tuple by default
def calc(*numbers):
	sum = 0 
	for n in numbers:
			sum += n * n
	return sum