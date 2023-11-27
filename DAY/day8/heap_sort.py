import heapq

# coding=utf-8
import random
import sys


def heap_sort(array):
	first = len(array)//2 - 1
	for start in range(first, -1, -1):
		print(start)
		# 从下到上，从右到左对每个非叶节点进行调整，循环构建成大顶堆
		big_heap(array, start, len(array) - 1)
	print(array)
	for end in range(len(array) - 1, 0, -1):
		# 交换堆顶和堆尾的数据
		array[0], array[end] = array[end], array[0]
		# 重新调整完全二叉树，构造成小顶堆
		big_heap(array, 0, end - 1)
		print(array)
	return array


def big_heap(array, start, end):
	root = start
	# 左孩子的索引
	child = root * 2 + 1
	while child <= end:
		# 节点有右子节点，并且右子节点的值大于左子节点，则将child变为右子节点的索引
		if child + 1 <= end and array[child] < array[child + 1]:
			child += 1
		if array[root] < array[child]:
			# 交换节点与子节点中较大者的值
			array[root], array[child] = array[child], array[root]
			# 交换值后，如果存在孙节点，则将root设置为子节点，继续与孙节点进行比较
			root = child
			child = root * 2 + 1
		else:
			break


if __name__ == '__main__':
	import time
	# array =list(range(1,1000000))
	# random.shuffle(array)
	# print(random.shuffle(list(range(1,10))))
	array=[5, 19, 9, 1, 7, 13, 17, 3, 11, 150,2,3,0,19,23,29,8]
	print(array)
	# big_heap(array,0,2)
	# print(array)
	# sys.exit()
	start=time.time()
	heap_sort(array)
	end=time.time()
	print(end-start)
	# start1 = time.time()
	# heapq.merge(array,key=len(array)-1,reverse=True)
	# end1 = time.time()
	# print(end1-start1)
	print(array)

	# print(heap_sort(array))