# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		l = []
		if root == None:
			return l
		if root.left!=None:
			l = l+self.inorderTraversal(root.left)
		l = l+[root.val]
		if root.right!=None:
			l = l+self.inorderTraversal(root.right)	
		return l

if __name__ == '__main__':
	s = Solution()
	root = TreeNode(0)
	r1 = TreeNode(1)
	r2 = TreeNode(2)
	r3 = TreeNode(3)
	r4 = TreeNode(4)
	r5 = TreeNode(5)
	root.left = r1
	root.right = r2
	r1.right = r3
	r3.left = r4
	r2.left = r5
	print s.inorderTraversal(root)
