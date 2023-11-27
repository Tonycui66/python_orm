"""
# ``test_h``
# 	>>> a = normalize(3920)
# 	>>> print(a)
# 	(1, 5, 20)

"""
from typing import Union,Tuple


def normalize(s: float) -> Tuple[int,int,float]:
	m,r = divmod(s,60)
	h,m = divmod(m,60)
	return int(h),int(m),r

def test(a: Union[slice]):
	if isinstance(a,slice):
		print("slice %s"%a)
		print(a.start)
		print(a.stop)
		print(a.step)
	else:
		print(a)
		# raise TypeError

class test_clsitem():
	h :int
	_m : int
	_s : int

	def __class_getitem__(cls, item: Union[Tuple,str]):
		if isinstance(item,Tuple):
			if len(item) > 3:
				h,m,s = item[:3]
			else:
				h,m,s = item
		elif isinstance(item,str):
			h,m,s = tuple(item.split(":"))
		return test_clsitem(int(h),int(m),float(s))

	def __init__(self,h,m=0,s=0):
		print("__init__")
		self.h = int(h)
		self.m = int(m)
		self.s = float(s)

	def __repr__(self):
		return str(self.h*3600+self.m*60+self.s)

	def __float__(self):
		return float(self.h *3600 + self.m * 60 + self.s)

	def __iter__(self):
		yield self.h
		yield self.m
		yield self.s

	def __add__(self,other):
		if not isinstance(other,test_clsitem):
			return NotImplemented
		return test_clsitem(*(a+b for a,b in zip(self,other)))


if __name__ == '__main__':
	# a= [1,2,3,4,5,6,7,8,9]
    # parts =slice(a[1:2])
    # print(parts)
    # print(parts.stop)
    # print(parts.start)
    # test(slice(1,2,3))
    # obj = slice(0,9,2)
    # print(a[obj])
    # test(obj)
	h,m,s = (1,2,3)
	print(h,m,s)
	tclsitem = test_clsitem(1,2,3.2)
	print(tclsitem.__slots__)
	tclsitem1 = test_clsitem(1,2,3.2)
	print(str(tclsitem))
	print(float(tclsitem))
	print(float(tclsitem+tclsitem1))
	a=[1,2,3,4,5]
	b=[6,7,8,9,10]
	print(*(a+b for a,b in zip(a,b)))