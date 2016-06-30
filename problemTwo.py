def evens(upperbound):
	a,b = 0, 1
	while a < upperbound:
		if (a%2 != 0):
			yield a
		a, b = b, a + b

print sum(evens(4000000))