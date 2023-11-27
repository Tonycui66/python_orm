## lazy buffer
class Path_1():
	def __init__(self,s):
		self.s = s
		self.buf = []
		self.w = 0

	def append(self,val):
		if not self.buf:
			self.buf = [None]*len(self.s)
			self.buf[0] = val
			self.w+=1
		else:
			self.buf[self.w] = val
			self.w+=1


	def index(self,i):
		if not self.buf:
			return self.s[i]
		return self.buf[i]

	def res(self):
		if not self.buf:
			return "".join(self.s[:self.w])
		return "".join(self.buf[:self.w])
##
def path_1(s):
	if len(s)=="":
		return '.'
	n = len(s)
	p = Path_1(s)
	rooted = s[0] == '/'
	r,dotdot = 0,0
	if rooted:
		r,dotdot = 1,1
		p.append('/')
	while r<n:
		if s[r] == '/':
			r+=1
		elif s[r] == '.' and (r+1 == n or s[r+1] == '/' ):
			r+=2
		elif s[r] == '.' and s[r+1] == '.' and ( r+2 == n or s[r+2] == '/'):
			r+=2
			if p.w > dotdot:
				p.w-=1
				while p.w > dotdot and p.index(p.w) != '/':
					p.w-=1
			elif not rooted:
				if p.w >0:
					p.append('/')
				p.append('.')
				p.append('.')
				dotdot = p.w
		else:
			if rooted and p.w != 1 or not rooted and p.w !=0:
				p.append('/')
			while r< n and s[r]!='/':
				p.append(s[r])
				r+=1
	if p.w == 0:
		return "."
	return p.res()


if __name__ == '__main__':
	str1 = "/../cxm/..//123.txt,123131"
	print(path_1(str1))
	# print(int(0))




