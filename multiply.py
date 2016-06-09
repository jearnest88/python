def multiply(a):
	x = a * 5
	return x

y = [2,4,10,16]
g = 0
while g < 4:
	b = y[g]
	result = multiply(b)
	print result
	g +=1

