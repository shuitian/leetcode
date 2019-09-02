# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

def print_list(node):
	s = ''
	while node:
		s += str(node.val)
		node = node.next
		if node:
			s += '->'
	print s

def build_list(val_list):
	if not val_list:
		return None
	head = ListNode(val_list[0])
	head_t = head
	for x in val_list[1:]:
		next = ListNode(x)
		head.next = next
		head = next

	return head_t

class Solution(object):
	def mergeKLists(self, lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		head = ListNode(0)
		tail = head
		node = True
		while node:
			node = self.get_min_node(lists)
			if not node:
				return head.next

			tail.next = node
			tail = node
			lists.remove(node)
			next = node.next
			if next:
				lists.append(next)
		return head.next


	def get_min_node(self, lists):
		min_node = None
		for node in lists:
			if not node:
				continue

			if min_node is None or node.val < min_node.val:
				min_node = node
		return min_node

if __name__ == '__main__':
	s = Solution()
	h1 = build_list([1,4,5])
	print_list(h1)
	h2 = build_list([1,3,4])
	print_list(h2)
	h3 = build_list([2,6])
	print_list(h3)

	h = s.mergeKLists([h1,h2,h3])
	print_list(h)

	h = s.mergeKLists([build_list([])])
	print_list(h)