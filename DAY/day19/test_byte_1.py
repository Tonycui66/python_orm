if __name__ == '__main__':
    str1 = "好"
    str1_byte = str1.encode("utf-8")
    str1_byte2 = str1.encode("GBK")
    # # result = str1_byte.replace(b'\x00'.encode('utf-8'), b'0'.encode('utf-8'))
    # result = str1_byte.replace(b''.encode('utf-8'), b'0'.encode('utf-8'))
    print(str1_byte)
    print(str1_byte2)
    # print(len(str1))
    # print(len(str1_byte))
    # print(len(str1_byte2))
    stby_src="\\0x"
    stby_0="\\0x"
    for b1 in str1_byte:
	    stby_src+=(hex(b1)[2:])
	    stby_0+="00"

    for b1 in str1_byte2:
	    print(hex(b1))
byte_code = bytearray(str1_byte)
print(stby_0,stby_src)
print(byte_code)
byte_code.replace(b'\xe5', b'0')
print(bytes(byte_code))
for i in stby_0.encode("utf-8"):
	print(i)