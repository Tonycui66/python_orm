import ast
import os
import yaml
# from ruamel import yaml

func_def = """
def add(x,y):
	return x+y
print(add(3,5))
"""

def bubble_sort(aa):
	n = len(aa)
	for i in range(n):
		for j in range(0,n-i-1):
			if aa[j] > aa[j+1]:
				aa[j],aa[j+1] = aa[j+1],aa[j]
if __name__ == '__main__':

	cm = compile(func_def,'<string>','exec')
	exec(cm)
	r_node = ast.parse(func_def)
	print(r_node)
	aa = {"aa":[(1,2),(3,4)],"bb":2,"cc":3}
	with open("dict_1.yaml",'w') as f:
		yaml.dump(aa,f)
	if os.path.exists("dict_1.yaml"):
		with open("dict_1.yaml",'r') as f:
			msg = yaml.load(f.read(),Loader=yaml.Loader)
			print(msg)
			print("读取出来的数据类型为:",type(msg))


	import yaml

	# 写YAML文件
	data = {'name': 'John', 'age': 30}
	with open('data.yaml', 'w') as f:
		yaml.dump(data, f)

	# 读YAML文件
	with open('data.yaml', 'r') as f:
		data = yaml.safe_load(f)
	print(data)


	aa = [100.33,22,110,82]
	print(aa)
	bubble_sort(aa)
	print(aa)
	for i in range(len(aa)):
		print(aa[i])


	def bubble_sort(arr):
		n = len(arr)
		for i in range(n):
			for j in range(0, n-i-1):
				if arr[j] > arr[j+1]:
					arr[j], arr[j+1] = arr[j+1], arr[j]

	arr = [64, 34, 25, 12, 22, 11, 90]
	bubble_sort(arr)
	print("排序后的数组：")
	for i in range(len(arr)):
		print("%d" % arr[i])


