import time
from random import random


def bisect_right(a, x, lo=0, hi=None):
	"""Return the index where to insert item x in list a, assuming a is sorted.

	The return value i is such that all e in a[:i] have e <= x, and all e in
	a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
	insert just after the rightmost x already there.

	Optional args lo (default 0) and hi (default len(a)) bound the
	slice of a to be searched.
	"""

	if lo < 0:
		raise ValueError('lo must be non-negative')
	if hi is None:
		hi = len(a)
	while lo < hi:
		mid = (lo+hi)//2
		if x < a[mid]: hi = mid
		else: lo = mid+1
	return lo


def bisect_test(a,x,lo=0,hi=None):
	if lo < 0:
		raise ValueError('lo must be non-negative')
	if hi is None:
		hi = len(a)
	if lo < hi:
		mid = (lo+hi)//2
		if x < a[mid]:
			hi = mid
		else:
			lo = mid+1
	return lo

def bisect_right_insert(a:list,x,lo=0,hi=None):
	l1 = bisect_test(a,x,lo,hi)
	print(l1)
	a.insert(l1,x)
	# return a

def bisect_test_left(a:list,x,lo=0,hi=None):
	if lo < 0:
		raise ValueError("lo must be non-negative")
	if hi is None:
		hi = len(a)
	while lo < hi:
		mid = (lo+hi)//2
		if x > a[mid]:
			hi = mid
		else:
			lo = mid + 1
	return lo

def bisect_left_insert(a:list,x,lo=0,hi=None):
	l1 = bisect_test_left(a,x,lo,hi)
	print(l1)
	a.insert(l1,x)



if __name__ == '__main__':
	# a = [1,3,5,7,9,11]
	import bisect
	a = list(range(1,100000000,3))
	# b = a.reverse()
	# print(bisect_right(a,8))
	# print(bisect_test(a,100000000))
	starttime = time.time()
	bisect_right_insert(a,10000000)
	# bisect.bisect(a,10000000)
	endtime = time.time()
	print("cost %s s"%str(endtime - starttime))
	# print(a)
	# a.reverse()
	# print(a)
	b = [11,9,7,5,3,1]
	print(bisect_left_insert(b,8))
	print(b)
	# rando
	# print(random.randrange(14))