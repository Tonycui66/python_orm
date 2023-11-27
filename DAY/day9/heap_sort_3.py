def sort_bigheap(array,start,end):
	root=start
	child=2*start+1
	print(root,"root",child,"child")
	while child <= end:
		if child+1 <=end and array[child] <array[child+1]:
			child+=1
			# print("child",child)
			# print("start",array[child],array[child+1])
			# array[child],array[child+1] = array[child+1],array[child]
			# print("end",array[child],array[child+1])
		if array[root]<array[child]:
			array[root],array[child] = array[child],array[root]
			root=child
			child=2*root + 1
		else:
			break
		# print(array)


def gen_bigheap(array):
	first=len(array)//2 - 1
	print(first)
	for start in range(first,0,-1):
		print(start,"first")
		sort_bigheap(array,start,len(array)-1)
		# print(array)
	for end in range(len(array)-1,-1,-1):
		array[0],array[end] = array[end],array[0]
		sort_bigheap(array,0,end-1)
	return array



if __name__ == '__main__':
    array=[120,4,23,9,28,78,93]
    print(gen_bigheap(array))