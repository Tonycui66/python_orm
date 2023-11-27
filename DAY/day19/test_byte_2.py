import sys
def zero_string(s):
	zero_str = ""
	print(s)
	for i, c in enumerate(s):
		print(i,c)
		if len(c.encode("utf-8")) == 1:
			zero_str += "0"
		else:
			for i in range(len(c.encode("utf-8"))):
				zero_str += "0"
			# zero_str += chr(ord(c) - ord('0'))
	return zero_str

s = "hello好"
s1= s.encode("utf-8")
# for b in s1:
# 	print(b)
# print(len(bytes("好".encode("utf-8"))))
# sys.exit()
result = zero_string(s)
print(result)

