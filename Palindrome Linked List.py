# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		values = []
		while head:
			values.append(head.val)
			head = head.next
		return values == values[::-1]

if __name__ == '__main__':
	class ListNode(object):
		def __init__(self, x):
			self.val = x
			self.next = None
	s = Solution()
	node = ListNode(1)
	node.next = ListNode(2)
	node.next.next = ListNode(1)
	print s.isPalindrome(node)
	node.next.next.next = ListNode(1)
	print s.isPalindrome(node)