import time
def check_non_negative(index):
	def validator(func):
		def wrapper(*args,**kwargs):
			if args[index] < 0:
				raise ValueError("Argument must be non-negative")
			return func(*args,**kwargs)
		return wrapper
	return validator

@check_non_negative(1)
def create_list(value,size):
	return [value] * size


def memoize(func):
	cache = {}
	def wrapper(*args):
		if args in cache:
			return cache[args]
		result = func(*args)
		cache[args] = result
		return result
	return wrapper

@memoize
def fibonacci(n):
	if n < 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)



if __name__ == '__main__':
    aa = create_list('a',3)
    start = time.time()
    print(fibonacci(300))
    end = time.time()
    print(end,start)
    start1= time.time()
    print(fibonacci(300))
    end1 = time.time()
    print(end1,start1)
    print(aa)
    aa = create_list('a',-1)