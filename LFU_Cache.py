class Node(object):
	"""docstring for Node"""
	def __init__(self, key, value):
		super(Node, self).__init__()
		self.key = key
		self.value = value
		self.next = None
		self.pre = None
		self.count = 1

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self):
		super(LinkedList, self).__init__()
		self.head = None
		self.tail = None

	def put(self, node):
		node.next = self.head
		if self.head:
			self.head.pre = node
		self.head = node
		if not self.tail:
			self.tail = node
		node.pre = None
	
	def remove_node(self, node):
		if node.pre:
			node.pre.next = node.next
		elif self.head == node:
			self.head = node.next

		if node.next:
			node.next.pre = node.pre
		elif self.tail == node:
			self.tail = node.pre

	def is_empty(self):
		return not self.head

class LFUCache(object):

	def __init__(self, capacity):
		"""
		:type capacity: int
		"""
		self.min = None
		self.linked_dict = {}
		self.data = {}
		self.capacity = capacity

	def get(self, key):
		"""
		:type key: int
		:rtype: int
		"""
		node = self.data.get(key, None)
		if not node:
			return -1

		linked_list = self.linked_dict[node.count]
		linked_list.remove_node(node)
		if linked_list.is_empty():
			del self.linked_dict[node.count]
			if self.min == node.count:
				self.min += 1

		node.count += 1
		linked_list = self.linked_dict.setdefault(node.count, LinkedList())
		linked_list.put(node)
		return node.value

	def put(self, key, value):
		"""
		:type key: int
		:type value: int
		:rtype: None
		"""
		if not self.capacity:
			return

		node = self.data.get(key, None)
		if node:
			node.value = value
			self.get(key)
			return
			
		if len(self.data) >= self.capacity:
			linked_list = self.linked_dict[self.min]
			del self.data[linked_list.tail.key]
			linked_list.remove_node(linked_list.tail)
			if linked_list.is_empty():
				del self.linked_dict[self.min]

		self.min = 1
		linked_list = self.linked_dict.setdefault(self.min, LinkedList())
		node = Node(key, value)
		self.data[key] = node
		linked_list.put(node)

def output(c):
	for count, linked_list in c.linked_dict.iteritems():
		print '    count',count
		k = linked_list.head
		s = 'head:'
		i= 0
		while k and i < 14:
			i += 1
			s += str(k.key) + ' '
			k = k.next

		s += '\ntail:'
		k = linked_list.tail
		i= 0
		while k and i < 14:
			i += 1
			s += str(k.key) + ' '
			k = k.pre
		print s
		

def test():
	cache = LFUCache(2)

	print cache.put(2, 1)
	# output(cache)
	print cache.put(2, 2)
	# output(cache)
	print cache.get(2)
	# output(cache)
	print cache.put(3, 3)
	print cache.put(4, 4)
	print cache.get(2)
	print cache.get(3)
	print cache.get(4)
	
if __name__ == '__main__':
	test()

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)