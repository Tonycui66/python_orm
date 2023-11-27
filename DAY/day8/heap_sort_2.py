import random
def heap_sort(array):
	first = len(array)//2 - 1
	for start in range(first,-1,-1):
		big_heap(array,start,len(array)-1)
	return array

def big_heap(array,start,end):
	root=start
	child=start*2 + 1
	while child <=end:
		if child+1<end and array[child]<=array[child+1]:
			child+=1
		if array[root] < array[child]:
			array[root],array[child] = array[child],array[root]
			root=child
			child=2*root+1
		else:
			break
	pass

def test_map(*iterable):
	# order,it = enumerate(map(iter,iterable))
	h=[]
	rh=[]
	rh_append=rh.append
	h_append=h.append
	for order,it in enumerate(map(iter,iterable)):
		try:
			next = it.__next__
			h_append([next(),1,next])
		except StopIteration:
			pass
	for lin in h:
		# i=0
		rh_append(lin[0])
		while True:
			try:
				rh_append(lin[2]())
			except StopIteration:
				break
	return rh

if __name__ == '__main__':
    array=[5, 19, 9, 1, 7, 13, 17, 3, 11, 150]
    # random.shuffle(array)
    print(array)
    big_heap(array,0,len(array)-1)
    print(array)
    print(heap_sort(array))
    a=[1,2,3]
    b=[4,5,6]
    c=[7,8,9]
    print(test_map(a,b,c))

