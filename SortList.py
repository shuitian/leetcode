# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode\
	def sortList(self, head):
		l = []
		p = head
		while p != None:
			l.append(p.val)
			p = p.next
		# print l
		l = sorted(l)
		p = head
		step = 0
		while p != None:
			p.val = l[step]
			p = p.next
			step = step +1
		return head


if __name__ == '__main__':
	head = ListNode(5)
	p2 = ListNode(3)
	p3 = ListNode(7)
	p4 = ListNode(4)
	p5 = ListNode(6)
	p6 = ListNode(2)
	head.next = p2
	p2.next = p3
	p3.next = p4
	p4.next = p5
	p5.next = p6

	s = Solution()
	head = s.sortList(head)
	head = s.sortList(head)