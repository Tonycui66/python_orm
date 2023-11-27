




if __name__ == '__main__':
	aa=["abcd","--datapath=1231","""--datapath=/data1/data1/node_master,qianstore=[Options]  mem_table_size=268435456 [Level \\"0\\"] compression=NoCompression [Level  \\"1\\"] compression=NoCompression [Level \\"2\\"] compression=NoCompression [Level \\"3\\"] compression=NoCompression [Level \\"4\\"] compression=NoCompression [Level \\"5\\"] compression=NoCompression [Level \\"6\\"] compression=NoCompression"""]
	print(aa.count("--datapath"))
	match = next(item for item in aa if item.startswith("--datapath"))
	print(match)
	print(aa.index(match))
	aa2=match.split(",")
	if len(aa2)==1:
		pass
	else:
		dir_path=aa2[0]
		qianstore_pt = aa2[1].split("qianstore=")[1]
		aa[aa.count(match)]=dir_path + "," + "qianstore=" + "'" + qianstore_pt + "'"
		print(aa[1])
	print(" ".join(aa))

	# print(match)