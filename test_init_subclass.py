#!/usr/bin/env python3

class Wrong:

	def __init_subclass__(subclass):
		subclass.__slots__ = ('x', 'y')


class Klass0(Wrong):
	pass

class Correct1(type):

	def __new__(meta_cls, cls_name, bases, cls_dict):
		cls_dict['__slots__'] = ('x', 'y')
		return super().__new__(
			meta_cls, cls_name, bases, cls_dict)


class Klass1(metaclass=Correct1):
	pass

o = Klass1()
# try:
# 	o.z = 3
# except AttributeError as e:
# 	print('Raised as expected:', e)


class Correct2(type):
	def __prepare__(name, bases):
		return dict(__slots__=('x', 'y'))

class Klass2(metaclass=Correct2):
	pass

o = Klass2()
# try:
# 	o.z = 3
# except AttributeError as e:
# 	print('Raised as expected:', e)


if __name__ == '__main__':
    wr = Klass0()
    wr.z = 3
    print(wr.__slots__)
    print(wr.z)
    o = Klass2()
    o.x = 3
    print(o.x)