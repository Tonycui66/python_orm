# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# """
# ``__class_getitem__``
# ``H``
# >>> H = test1()
# >>> ArithmeticError
# >>> os
# >>> sys
# """
import math


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def test1():
    return "abac"


#!/usr/bin/env python3

class Foo(type):
    @property
    def bar(self):
        return self._bar

    @bar.setter
    def bar(self, value):
        self._bar = value

    def __setattr__(self, name, value):
        print(f'setting {name!r} to {value!r}')
        super().__setattr__(name, value)

    def __new__(meta_cls, cls_name, bases, cls_dict):
        cls_dict(__slots__=('x','y'))
        return super().__new__(meta_cls,cls_name,bases,cls_dict)



if __name__ == '__main__':
    # print_hi('PyCharm')
    # fo = Foo()
    # fo.bar = 8
    # print(fo._bar)
    # print(fo.bar)
    # print(fo.__slots__)
    # # g = {"abc":1}
    # # l = {}
    # # exec("age=abc+1",g,l)
    # # print(g.get("abc"))
    # # print(l.get("age"))
    # # print(l.get("abc"))
    # g = {"abc":10,"test1":test1}
    # l = {"age":2}
    # print(eval('(abc+1)*age',g,l))
    # print(l)
    # print(eval('test1()+"123"',g))
    print(math.hypot(3,4))
    print(math.hypot(12,4,5))



