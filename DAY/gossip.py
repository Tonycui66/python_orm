import random


class Node:
	def __init__(self,id,data):
		self.id = id
		self.data = data


	def gossip(self,other):
		self.data = other.data = (self.data + other.data)/2



if __name__ == '__main__':
    nodes = [Node(i,random.randint(1,100)) for i in range(1,6)]
    for i in range(10000):
        node_a,node_b = random.sample(nodes,2)
        node_a.gossip(node_b)

    for node in nodes:
	    print(node.id,node.data)