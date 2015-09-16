# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	#FIXME it does not fixed by insert sort
    # @param head, a ListNode
    # @return a ListNode
	def insertionSortList(self, head):
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