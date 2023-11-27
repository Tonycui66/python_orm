import threading


def Singleton(cls):

	_instance = {}

	def _singleton(*args, **kargs):
		if cls not in _instance:
			_instance[cls] = cls(*args, **kargs)
		return _instance[cls]

	return _singleton


@Singleton
class A(object):
	a = 1

	def __init__(self, x=0):
		import time
		time.sleep(1)
		self.x = x

class Single_install_cls():
	__Cls_lock = threading.Lock()

	def __init__(self):
		import time
		time.sleep(1)

	@classmethod
	def instance(cls,*args,**kwargs):
		if not hasattr(Single_install_cls,"_instance"):
			with Single_install_cls.__Cls_lock:
				if not hasattr(Single_install_cls,"_instance"):
					Single_install_cls._instance = cls(*args,**kwargs)
		return Single_install_cls._instance

class Single_install(object):
	__Cls_lock = threading.Lock()

	def __init__(self):
		pass

	def __new__(cls,*args,**kwargs):
		if not hasattr(Single_install,"_instance"):
			with Single_install.__Cls_lock:
				if not hasattr(Single_install,"_instance"):
					Single_install._instance = object.__new__(cls)
		return Single_install._instance

def task(cls):
	obj = cls()
	print(obj)

if __name__ == '__main__':
    a1 = A(2)
    a2 = A(3)
    print(a1.x)
    a2.x = 10
    print(a1.x)
    import time
    timestart = time.time()
    # for num in range(10):
    #     t = threading.Thread(target=task,name="thread%s"%str(num),args=(Single_install_cls,))
    #     t.start()
    print("timeend %s s"%str(time.time() - timestart))


    for num in range(10):
	    t = threading.Thread(target=task,name="thread%s"%str(num),args=(Single_install,))
	    t.start()
