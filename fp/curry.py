def curry_add(a):
	def f(b):
		return a + b
	return f

def add3(x, y, z):
	return x + y + z

# @curry(2)
# def is_in(x: str, y:str) -> bool:

# @curry(2)
# def settled(towns: tuple[str],
#         nomad: str) -> tuple[str, bool]:
#     return (nomad,
#         reduce(lambda x, y: x or y,
#             map(is_in(nomad), towns))
# print(map(curry_add(1), (1, 2)))
print(curry_add(1)(1)) #ex 1

