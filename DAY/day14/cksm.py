# 计算SUM校验和
def sum_checksum(data):
	checksum = 0
	for byte in data:
		# print(byte)
		checksum += byte
	return checksum

# 特殊方式计算
def special_type(data,crc_poly):
	checksum = 0
	for byte in data:
		checksum ^=byte
		for i in range(8):
			if checksum & 0x01:
				checksum = (checksum >>1) ^ crc_poly
			else:
				checksum >>=1
	return checksum
if __name__ == '__main__':
	# 待校验数据
	data = b'hello1world'
	data1 = b'hello world'

	# 计算校验和
	checksum = sum_checksum(data)
	print(checksum)

	checksum1 = sum_checksum(data1)
	print(checksum1)
	f = open("./data",'+rb')
	fdata = f.readlines()[0]
	print(fdata)
	fchecksum = sum_checksum(fdata)
	print(fchecksum)
	f1 = open("./data1",'+rb')
	fdata1 = f1.readlines()[0]
	print(fdata1)
	fchecksum1 = sum_checksum(fdata1)
	print(fchecksum1)
	chsum = 10
	chsum >>=1
	print(chsum)
	chsum1 = 10
	chsum1 >>=1
	print(chsum1>>1)
	special_checksum = special_type(data1,0x1021)
	print(special_checksum)
	special_checksum0 = special_type(data,0x1021)
	print(special_checksum0)
	# 1010
	# 0101
	# 10100
