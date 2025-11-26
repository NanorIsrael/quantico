def curry_add(a):
	def f(b):
		return a + b
	return f



# print(map(curry_add(1), (1, 2)))
print(curry_add(1)(1)) #ex 1