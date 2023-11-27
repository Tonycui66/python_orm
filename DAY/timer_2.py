def my_decorator(value):
	def inner_function(original_function):
		def wrapped_function(*args, **kwargs):
			print(f"The value passed to the decorator is {value}")
			return original_function(*args, **kwargs)
		return wrapped_function
	return inner_function

@my_decorator("hello world")
def my_function(x):
	print(x+1)
	return x + 1

result = my_function(3)
# print(result)