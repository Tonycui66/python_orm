'''
自定义checksum算法实现
checksum：校验和
data：需要校验的数据
'''
import math
from functools import reduce

import numpy as np

class myCheckSum():
	def __init__( self,checkSum,data=[] ):
		self.checkSum=checkSum
		self.data=data
		self.hexadecimal={ 'a':10, 'b':11, 'c':12, 'd':13, 'e':14,  'f':15,
		                   10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}      #  十六进制大于9的数
		self.sumdata=0x0

		#第一步，求和（遍历时遇到checksum，替换为0x0）
		datas=self.sumCheckSum()
		print(len(self.sumdata))
		print("datas:",datas)
		#第二步，将进位加到低位
		cal=self.carryAddLow( len(self.sumdata),datas ) # len(self.sumdata)=5     cal=0x4ad1
		print("cal:",cal)

		#第三步，取补码
		result=self.complementData(cal)
		print('result:',result)
		print('checksum:',checkSum)   #   checkSum: 46382
		if result==checkSum:
			print('True：正确')
		else:
			print('False：错误')


	# 求和
	def sumCheckSum(self):
		dataLen=len(self.data)

		for i in range(dataLen):
			if self.data[i]==self.checkSum:  # 找到checksum
				self.sumdata+=0x0   #  checksum替换为0x0来累加
			else:
				self.sumdata+=self.data[i]
		#print( type( sel.SumData ) )      #  215758  <class 'int'>  int型
		self.sumdata=hex(self.sumdata)[2:]     #  '0x34ace'    str类型   十六进制

		datas=[]
		print(self.sumdata)
		for i in self.sumdata:
			if i in ['a','b','c','d','e','f']:
				datas.append( self.hexadecimal[i] )
			else:
				datas.append( int(i) )
				#print( 'datas:',datas)    #  ['3','4','10','12','14']
		return datas


	# 取反 ，这里取反取的是补码   在python中 ~ 不能取到补码
	def complementData(self,cal):
		tenResult=int(cal,16)
		twoResult=bin(tenResult)

		calLen=len( cal[2:])  #  4
		twoResultLen=len( twoResult[2:])    #   15
		if calLen*4>twoResultLen:
			subLen=calLen*4-twoResultLen      #   1
			twoResult='0'*subLen+twoResult[2:]
		else:
			twoResult=twoResult[2:]
		#print( 'twoResult:',twoResult ,'*type:',type(twoResult))    # twoResult: 0100101011010001 *type: <class 'str'>

		reverseResult='0b'
		print("twoResult:",twoResult)
		# twoResult=twoResult[2:]
		for i in twoResult:
			if i=='1':
				reverseResult+='0'
			else:
				reverseResult+='1'
		print('reverseResult:',reverseResult)  #  reverseResult: 0b1011010100101110
		print("hex:",hex( eval(reverseResult) ) )      #   0xb52e
		return eval(reverseResult)    #   46382  十进制



	#  进位加到低位     返回一个十六进制数
	#  将32bit值的高16bit与低16bit相加到一个新的32bit值中，若新的32bit值大于0Xffff, 再将新值的高16bit与低16bit相加；
	def carryAddLow(self,sumDataLen,datas):    #   sumDataLen=5  判断是否大于0Xffff，一种直接数值判断，另一种长度大于0Xffff的四位
		bus,rem=divmod(sumDataLen,4)  # 取bus商  rem余数

		dualLists=[]
		if rem != 0:
			for i in range(bus+1):   # 如果有余数  bus需要+1
				dualLists.append([])   # dualLists=[ [], [], []]
				if i==0:         # 第一个list为 [0,0,0,3]
					for j in range(4-rem):
						dualLists[i].append(0)
					for j in range(rem):
						dualLists[i].append( datas[0] )
						del datas[0]
				else:
					for j in range(4):
						dualLists[i].append( datas[0] )
						del datas[0]
		else:
			for i in range(bus):
				dualLists.append([])
				for j in range(4):
					dualLists[i].append( datas[0] )
					del datas[0]
		#print( 'dualLists:',dualLists)    #  dualLists: [[0, 0, 0, 3], [4, 10, 12, 14]]
		print("dualLists:",dualLists)
		res=[0,0,0,0]
		for i in range( len(dualLists)):
			res=np.array(res)+np.array( dualLists[i] )    #  使用numpy中array把两个list相加
		#print('res:',res)    #  res: [ 4 10 12 17]    到这里进位加到低位结束
		print('res:',res)

		result=[]
		for i in range( len(res)-1,-1,-1 ):    #  逆序遍历res
			if res[i]>15:    #  大于15的进位  小于等于的直接存了
				result.append( res[i]%16 )
				res[i-1]+=res[i]//15      ###################################################
			else:
				result.append( res[i] )
		#print('result:',result)

		data='0x'
		for i in range( len(result)-1,-1,-1 ):
			if result[i] in [10,11,12,13,14,15]:
				data+=self.hexadecimal[ result[i] ]
			else:
				data+=str( result[i] )
		#print('data:',data)   #   4ad1
		return data



if __name__ == '__main__':
	data = [0x4500,0x0030,0x804c,0x4000,0x8006,0xb52e,0xd343,0x117b,0xcb51,0x153d]
	print(reduce(lambda x, y: x + y, data))
	obj = myCheckSum(0xb52e,data)
	print(obj.carryAddLow(5,[ 3,15, 15, 14, 14]))
	import binascii
	str_data = "Hello,world!"
	hex_str = binascii.hexlify(str_data.encode('utf-8'))
	print(hex_str)
	data1 = [0x4865,0x6c6c,0x6f2c,0x776f,0x726c,0x6421]
	myCheckSum(0x776f,data1)






