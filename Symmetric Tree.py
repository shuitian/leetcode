# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return self._isSymmetric(root and root.left, root and root.right)


	def _isSymmetric(self, left, right):
		if not left and not right:
			return True

		if left and not right:
			return False

		if not left and right:
			return False

		if left.val != right.val:
			return False

		return self._isSymmetric(left.left,right.right) and self._isSymmetric(left.right,right.left)
		

if __name__ == '__main__':
	class TreeNode(object):
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

	s = Solution()
	node = TreeNode(1)
	node.left = TreeNode(2)
	node.right = TreeNode(2)
	node.left.left = TreeNode(3)
	node.left.right = TreeNode(4)
	node.right.right = TreeNode(3)
	node.right.left = TreeNode(4)
	print s.isSymmetric(node)
	print s.isSymmetric(None)