#-*- coding:utf8

class Test():
	def __init__(self):
		self.password1 = 10
	@property
	def password(self):
		print("pure password")
		print(self.password1)

	@password.setter
	def password(self,pwd):
		print("1231313131")
		self.password1 = pwd


if __name__ == '__main__':
    t = Test()
    pwd=102
    # t.password
    t.password = 123
    t.password