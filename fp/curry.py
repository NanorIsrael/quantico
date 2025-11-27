def curry_add(a):
	def f(b):
		return a + b
	return f

def add3(x, y, z):
	return x + y + z



# print(map(curry_add(1), (1, 2)))
print(curry_add(1)(1)) #ex 1

