class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		orderlist = []
		self.preorder(root,orderlist)
		return orderlist

	def preorder(self, root, orderlist):	
		if root:
			orderlist.append(root.val)
			self.preorder(root.left, orderlist)
			self.preorder(root.right, orderlist)

	def inorderTraversal(self, root):
		orderlist = []
		self.inorder(root, orderlist)
		return orderlist

	def inorder(self, root, orderlist):
		if root:
			self.inorder(root.left, orderlist)
			orderlist.append(root.val)
			self.inorder(root.right, orderlist)

	def postorderTraversal(self, root):
		orderlist = []
		self.postorder(root, orderlist)
		return orderlist

	def postorder(self, root, orderlist):
		if root:
			self.postorder(root.right, orderlist)
			orderlist.append(root.val)
			self.postorder(root.left, orderlist)

	def isValidBST(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		orderlist = self.inorderTraversal(root)
		for x in xrange(1,len(orderlist)):
			if orderlist[x]<=orderlist[x-1]:
				return False
		return True

if __name__ == '__main__':
	s = Solution()
	r1 = TreeNode(4)
	r2 = TreeNode(3)
	r3 = TreeNode(5)
	r4 = TreeNode(1)
	r5 = TreeNode(6)
	r6 = TreeNode(7)
	r7 = TreeNode(2)
	r1.left = r2;
	r1.right = r3;
	r2.left = r4;
	r4.right = r7
	r3.right = r5;	
	r5.right = r6;
	print s.isValidBST(r1)