from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
from urllib.parse import urlparse
from os.path import join,isfile

OK=1
FAIL=2
EMPTY=''
MAX_LENGTH = 6

def getport(url):
	"""
	:param url:
	:return:
	"""
	name = urlparse(url)
	print(name)
	ip = name.netloc.split(":")[0]
	port = name.netloc.split(":")[-1]
	return (ip,int(port))


class Node():

	def __init__(self,url,filepath,secret):
		"""
		:param url:  连接rpc服务器的url
		:param filepath: 共享文件的路径
		:param secret:  共享文件获取的密钥
		"""
		self.url = url
		self.filepath = filepath
		self.secret = secret
		self.know = set()

	def _start(self):
		ip,port = getport(self.url)
		s = SimpleXMLRPCServer((ip,port))
		s.register_instance(self)
		s.serve_forever()

	def hello(self,other):
		"""
		add  node url
		:param other:
		:return: 1
		"""
		self.know.add(other)
		return OK


	def query(self,query,history=[]):
		"""
		检查文件是否存在,向其它添加的节点查询，返回数据
		:param query:  获取的文件名称
		:param history: 最大处理的连接数
		:return:
		"""
		code,data = self._query(query)
		if code == OK: return code,data
		else:
			#如果没有查到就广播向其它节点查询
			history = history + self[self.url] #本url添加到查询记录
			if len(history) >= MAX_LENGTH:
				return FAIL,EMPTY
			return self._broadcast(query,history)

	def fetch(self,query,secret):
		"""
		调用查询,存储文件
		:param query:
		:param secret:
		:return:
		"""
		if secret != self.secret: return FAIL
		code,data = self.query(query)
		if code == OK:
			#正常返回了数据,将数据文件写入本地
			with open(join(self.filepath,query),'w') as f:
				f.write(data)
			return OK
		else:
			return FAIL


	def _broadcast(self,query,history):
		"""
		向其它节点广播并查询
		:param query: 获取的文件名称
		:param history: 最大处理的连接数
		:return:
		"""
		for other in self.know.copy(): # 因为这里的known()可能被remove(),因此copy()
			print("广播url:",other)
			if other in history:continue
			try:
				s = ServerProxy(other)
				code,data = s.query(query,history)
				if code == OK:
					return code,data
			except:
				self.know.remove(other)
		return FAIL,EMPTY #如果其他节点没有查到就返回空

	def _query(self,query):
		"""
		抽象查询的方法
		:param query:
		:return:
		"""
		dir = self.filepath
		name = join(dir,query)
		if not isfile(name): return FAIL,EMPTY
		return OK,open(name).read()

def main(url,filepath,secret):
	n = Node(url,filepath,secret)
	n._start()


def twice(x):
	return x*2
if __name__ == '__main__':
	# s = SimpleXMLRPCServer(("10.16.30.122",50000))
	# s.register_function(twice)
	# s.serve_forever()
	print(getport("http://10.16.30.122:50000"))
	main("http://10.16.30.122:50000","/home/cxm","123456")