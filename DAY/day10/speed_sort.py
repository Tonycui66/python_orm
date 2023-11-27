#ecoding:utf8








# def speed_sort(array):
	# start=array[0]
	# low = 0
	# high = len(array)-1
	# while True:
	# 	if low == high:
	# 		array[low]=start
	# 		break
	# 	if start < array[high]:
	# 		high-=1
	# 		continue
	# 	elif start > array[high]:
	# 		array[low] = array[high]
	# 		low+=1
	# 		if start < array[low]:
	# 			array[high] = array[low]
	# 			high-=1
	# 		else:
	# 			low+=1

"""
 privot
 left list
 right list
 repeat first second three step

"""
def speed_sort(array):
	start=array[0]
	low = 0
	high = len(array)-1
	while True:
		if low == high:
			array[low]=start
			break
		if start < array[high]:
			high-=1
		# continue
		elif start > array[high]:
			if low > len(array)-1:
				break
			array[low] = array[high]

			low+=1

			while True:
				if start < array[low]:
					array[high] = array[low]
					low+=1
					if low > len(array)-1:
						break
				# high-=1
				else:
					break
		else:
			continue

if __name__ == '__main__':
	aa = "{b}123"
	c1={"b":"1"}
	bb=aa.format(**c1)
	print(bb)
    # array = [11,9,8,6,4,3,2,1,18,7]
    # speed_sort(array)
    # print(array)
    # array=speed_sort(array)
    # print(array)