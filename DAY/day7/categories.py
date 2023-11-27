import sys
import collections

from unicodedata import category




def categroy_stats():
	counts = collections.Counter()
	first = {}
	print(sys.maxunicode)
	for code in range(sys.maxunicode + 1):
		# print(code)
		char = chr(code)
		# print(char)
		cat = category(char)
		if cat not in counts:
			first[cat] = char
		counts[cat]  +=1
	return counts,first




if __name__ == '__main__':
	for i in range(sys.maxunicode):
		if chr(i) == "崔":
			print(i)
	print(chr(23828))
	print(chr(11990),chr(11991))
	print(chr(11992))
	print(chr(20000))
	print(chr(20528))
	print(chr(33828))
	print(chr(38828))
	print(chr(38928))
	print(chr(38999))
	print(chr(40500))
	print(chr(40800))
	print(chr(40900))
	print(chr(40917)) # 最后一个汉字
	print(chr(43828))

	# print(collections.Counter())

	# print(categroy_stats())
	x=0
	y=0
	def test():
		x = 1
		print("x assignment %d"%x)
	def test2():
		y = 2
		print("y assignment %d"%y)
	test()
	test2()
	print(x,y)
