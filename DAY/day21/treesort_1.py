class Treesort(object):
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right


def treesort(arr):
	if not arr:
		return []
	root = Treesort(arr[0])
	for i in range(1,len(arr)):
		tree_add(root,arr[i])
	return inorder(root)

def tree_add(node,val):
	if not node:
		return Treesort(val)
	if node.val > val:
		node.left = tree_add(node.left,val)
	else:
		node.right = tree_add(node.right,val)
	return node

def inorder(node):
	if not node:
		return []
	res = []
	res +=inorder(node.left)
	res.append(node.val)
	res +=inorder(node.right)
	return res

if __name__ == '__main__':
    arr=[9,8,5,6,3,4,10]
    arr = treesort(arr)
    print(arr)
