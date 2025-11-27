from itertools import dropwhile, takewhile, compress, islice


def drop_while_example():
	return list(dropwhile(lambda x: x % 2 == 0, [4, 6, 8, 3, 2]))

def take_while_example():
	return list(takewhile(lambda x: x % 2 == 0, [4, 6, 8, 3, 2]))

def compress_example():
	nums = [4, 6, 8, 3, 2]
	mask = [x % 2 == 0 for x in nums]
	return list(compress(nums, mask))

def compress_example():
	nums = [4, 6, 8, 3, 2]
	mask = [x % 2 == 0 for x in nums]
	return list(compress(nums, mask))

def islice_example():
	nums = range(1000)
	return list(islice(nums, 100))

print(drop_while_example())
print(take_while_example())
print(compress_example())
print(islice_example())