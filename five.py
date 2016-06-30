def gcd(a,b):
	while b != 0:
		temp = b
		b = a % b
		a = temp
	return a

def lcm(a,b):
	return a * b / gcd(a,b)


n = 1
for x in range (2,20):
	n = lcm(n,x)
	print(n)