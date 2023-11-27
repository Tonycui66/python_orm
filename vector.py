import copy
import math

class test:
	pass

class Vector:

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Vector({self.x!r},{self.y!r})'

	def __add__(self, other):
		if not isinstance(other,Vector):
			raise TypeError
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x,y)

	def __abs__(self):
		return math.hypot(self.x,self.y)

	def __mul__(self, scalar):
		return Vector(self.x*scalar,self.y*scalar)

	def __bool__(self):
		return bool(abs(self))

def f():
	print(123)


if __name__ == '__main__':
	v1 = Vector(3,4)
	v2 = Vector(1,2)
	print(v1)
	print(v1+v2)
	print(abs(v1*3))
	print(abs(v1))
	t3 = test()
	# print(v1+t3)
	d = {
		"name" : "abc",
		"f" : f,
		"x" :123,
		"y" : 345,
	}

	A = type('A',(Vector,),d)
	B = type('B',(Vector,),d)
	print(A(12,23).name)
	print(A(1,2)+B(3,4))
	print(A.x,A(1,2).x)
	print(A.__dict__)
	print("v1.mro")
	# print(A.__name__)
	C=type("C",(Vector,),d)
	print(C.name)
	a={1:['a','a1','a2'],2:'b',3:'c'}
	b={4:'d',5:'e',6:'f'}
	a.update(b)
	b[4]='modify'
	print(a)
	print(b)
	c=a.copy()
	dc=copy.deepcopy(a)
	c[1].append('a3')
	c[2] = '2'
	print(a,c,dc)


