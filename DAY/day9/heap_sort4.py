import heapq


def sort4(array):
	first=len(array)//2 - 1
	print(first)
	for start in range(first,-1,-1):
		bigheap4(array,start,len(array)-1)
		# print(array)
	# for end in range(len(array)-1,0,-1):
	# 	array[0],array[end] = array[end],array[0]
	# 	bigheap4(array,0,end-1)
	return array



def bigheap4(array,start,end):
	root=start
	child=2*start + 1
	while child < end:
		if child + 1 <=end and array[child] < array[child+1]:
			child +=1
		if array[root] < array[child]:
			array[root],array[child]=array[child],array[root]
			root=child
			child=2*root+1
		else:
			break
		# print(array)


if __name__ == '__main__':
    array=[12,1,22,8,5,89]
    print(sort4(array))
    heapq.heapify(array)
    print(array)
    # heapq.heappush(array,13)
    # heapq.heappop(array)
    # print(array)
    # print(heapq.heappop(array))