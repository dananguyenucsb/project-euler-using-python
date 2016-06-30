import math

def pythag(a,b):
	temp = (a ** 2) + (b ** 2)
	return math.sqrt(temp)

def pythagTrip(a,b):
	sumOf = pythag(a,b) + a + b
	return sumOf

for x in range(1,1000):
	for n in range(x+1,1000):
		a = (n**2) - (x**2)
		b = 2 * x * n
		c = pythag(a,b)
		if a+b+c == 1000:
			product = a * b * c
print (product)




