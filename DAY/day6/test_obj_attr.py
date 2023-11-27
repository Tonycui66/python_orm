# -*- coding:utf-8 -*-
class Obj_attr(object):

	def __init__(self):
		self.abc = None


def final(f):
	print("set abc wrapper")
	f.abc=10
	return f

@final
class test_final():
	def __init__(self):
		print("obj set abc")
		self.abc = 20
		print("test final")

	def __call__(self,name):
		print(name)

if __name__ == '__main__':
    # obj = Obj_attr()
    # if not hasattr(obj, "abc"):
	#     pass
    # else:
	#     print("abc is exists !!!")
    A = test_final()
    print(A.abc)
    print(A(name=10))