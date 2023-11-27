class Tree(object):
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right





def insert(node,val):
	if not node:
		return Tree(val=val)
	if val < node.val:
		node.left = insert(node.left,val)
	else:
		node.right = insert(node.right,val)
	return node


def treesort(arr):
	if not arr:
		return []
	root = Tree(arr[0])
	for i in range(1,len(arr)):
		insert(root,arr[i])

	return inorder(root)


def inorder(node):
	if not node:
		return []
	res = []
	res +=inorder(node.left)
	res.append(node.val)
	res +=inorder(node.right)
	return res

if __name__ == '__main__':
    arr = [90,9,80,8,8,5,6,3,8,4,10]
    print(treesort(arr))