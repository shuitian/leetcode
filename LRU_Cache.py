class Node(object):
	"""docstring for Node"""
	def __init__(self, key, value):
		super(Node, self).__init__()
		self.key = key
		self.value = value
		self.next = None
		self.pre = None

class LRUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.head = None
		self.tail = None
		self.data = {}
		self.capacity = capacity

	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		node = self.data.get(key, None)
		if node:
			self.remove_node(node)
			self.set_first(node)
			return node.value
		return -1

	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: None
		"""

		node = self.data.get(key, None)
		if node:
			self.remove_node(node)

		if len(self.data) >= self.capacity:
			self.remove_node(self.tail)

		n = Node(key, value)
		self.set_first(n)

	def remove_node(self, node):
		if node.pre:
			node.pre.next = node.next
		else:
			self.head = node.next

		if node.next:
			node.next.pre = node.pre
		else:
			self.tail = node.pre

		del self.data[node.key]

	def set_first(self, node):
		node.next = self.head
		if self.head:
			self.head.pre = node
		self.head = node
		if not self.tail:
			self.tail = node
		node.pre = None
		self.data[node.key] = node

# def output(c):
# 	k = c.head
# 	s = ''
# 	i= 0
# 	while k and i < 14:
# 		i += 1
# 		s += str(k.key) + ' '
# 		k = k.next

# 	s += '\n'
# 	k = c.tail
# 	i= 0
# 	while k and i < 14:
# 		i += 1
# 		s += str(k.key) + ' '
# 		k = k.pre
		
# 	print s
# 	print c.data.keys()

# def test():
# 	c = LRUCache(10)
# 	print 'c.put(10,13)',c.put(10,13)
# 	print 'c.put(3,17)',c.put(3,17)
# 	print 'c.put(6,11)',c.put(6,11)
# 	print 'c.put(10,5)',c.put(10,5)
# 	print 'c.put(9,10)',c.put(9,10)
# 	print 'c.get(13)',c.get(13)
# 	print 'c.put(2,19)',c.put(2,19)
# 	print 'c.get(2)',c.get(2)
# 	print 'c.get(3)',c.get(3)
# 	print 'c.put(5,25)',c.put(5,25)
# 	print 'c.get(8)',c.get(8)
# 	print 'c.put(9,22)',c.put(9,22)
# 	print 'c.put(5,5)',c.put(5,5)
# 	print 'c.put(1,30)',c.put(1,30)
# 	print 'c.get(11)',c.get(11)
# 	print 'c.put(9,12)',c.put(9,12)
# 	print 'c.get(7)',c.get(7)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.get(8)',c.get(8)
# 	print 'c.get(9)',c.get(9)
# 	print 'c.put(4,30)',c.put(4,30)
# 	print 'c.put(9,3)',c.put(9,3)
# 	print 'c.get(9)',c.get(9)
# 	print 'c.get(10)',c.get(10)
# 	print 'c.put(6,14)',c.put(6,14)
# 	print 'c.put(3,1)',c.put(3,1)
# 	print 'c.get(3)',c.get(3)
# 	print 'c.put(10,11)',c.put(10,11)
# 	print 'c.get(8)',c.get(8)
# 	print 'c.put(2,14)',c.put(2,14)
# 	print 'c.get(1)',c.get(1)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.get(4)',c.get(4)
# 	print 'c.put(11,4)',c.put(11,4)
# 	print 'c.put(12,24)',c.put(12,24)
# 	print 'c.put(5,18)',c.put(5,18)
# 	print 'c.get(13)',c.get(13)
# 	print 'c.put(7,23)',c.put(7,23)
# 	print 'c.get(8)',c.get(8)
# 	print 'c.get(12)',c.get(12)
# 	print 'c.put(3,27)',c.put(3,27)
# 	print 'c.put(2,12)',c.put(2,12)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.put(2,9)',c.put(2,9)
# 	print 'c.put(13,4)',c.put(13,4)
# 	print 'c.put(8,18)',c.put(8,18)
# 	print 'c.put(1,7)',c.put(1,7)
# 	print 'c.get(6)',c.get(6)
# 	print 'c.put(9,29)',c.put(9,29)
# 	print 'c.put(8,21)',c.put(8,21)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.put(6,30)',c.put(6,30)
# 	print 'c.put(1,12)',c.put(1,12)
# 	print 'c.get(10)',c.get(10)
# 	print 'c.put(4,15)',c.put(4,15)
# 	print 'c.put(7,22)',c.put(7,22)
# 	print 'c.put(11,26)',c.put(11,26)
# 	print 'c.put(8,17)',c.put(8,17)
# 	print 'c.put(9,29)',c.put(9,29)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.put(3,4)',c.put(3,4)
# 	print 'c.put(11,30)',c.put(11,30)
# 	print 'c.get(12)',c.get(12)
# 	print 'c.put(4,29)',c.put(4,29)
# 	print 'c.get(3)',c.get(3)
# 	print 'c.get(9)',c.get(9)
# 	print 'c.get(6)',c.get(6)
# 	print 'c.put(3,4)',c.put(3,4)
# 	print 'c.get(1)',c.get(1)
# 	print 'c.get(10)',c.get(10)
# 	print 'c.put(3,29)',c.put(3,29)
# 	print 'c.put(10,28)',c.put(10,28)
# 	print 'c.put(1,20)',c.put(1,20)
# 	print 'c.put(11,13)',c.put(11,13)
# 	print 'c.get(3)',c.get(3)
# 	print 'c.put(3,12)',c.put(3,12)
# 	print 'c.put(3,8)',c.put(3,8)
# 	print 'c.put(10,9)',c.put(10,9)
# 	print 'c.put(3,26)',c.put(3,26)
# 	print 'c.get(8)',c.get(8)
# 	print 'c.get(7)',c.get(7)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.put(13,17)',c.put(13,17)
# 	print 'c.put(2,27)',c.put(2,27)
# 	print 'c.put(11,15)',c.put(11,15)
# 	print 'c.get(12)',c.get(12)
# 	print 'c.put(9,19)',c.put(9,19)
# 	print 'c.put(2,15)',c.put(2,15)
# 	print 'c.put(3,16)',c.put(3,16)
# 	print 'c.get(1)',c.get(1)
# 	print 'c.put(12,17)',c.put(12,17)
# 	print 'c.put(9,1)',c.put(9,1)
# 	print 'c.put(6,19)',c.put(6,19)
# 	print 'c.get(4)',c.get(4)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.get(5)',c.get(5)
# 	print 'c.put(8,1)',c.put(8,1)
# 	print 'c.put(11,7)',c.put(11,7)
# 	print 'c.put(5,2)',c.put(5,2)
# 	print 'c.put(9,28)',c.put(9,28)
# 	print 'c.get(1)',c.get(1)
# 	print 'c.put(2,2)',c.put(2,2)
# 	print 'c.put(7,4)',c.put(7,4)
# 	print 'c.put(4,22)',c.put(4,22)
# 	print 'c.put(7,24)',c.put(7,24)
# 	print 'c.put(9,26)',c.put(9,26)
# 	print 'c.put(13,28)',c.put(13,28)
# 	print 'c.put(11,26)',c.put(11,26)
	
# if __name__ == '__main__':
# 	test()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)