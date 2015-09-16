# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param preorder, a list of integers
	# @param inorder, a list of integers
	# @return a tree node
	def buildTree(self, preorder, inorder):
		if len(preorder) == 0:
			return None

		root = TreeNode(preorder[0])
		if len(preorder) == 1:
			return root

		root = TreeNode(preorder[0])
		index = inorder.index(preorder[0])
		
		
		# print "index:",index
		# print preorder[1:index+1], inorder[:index]		
		# print preorder[index+1:], inorder[index+1 :]

		root.left = self.buildTree(preorder[1:index+1], inorder[:index])
		root.right = self.buildTree(preorder[index+1:], inorder[index+1 :])
		return root



if __name__ == '__main__':
	s = Solution()
	P = [1,2,3,4,5,6,7,8]
	I = [3,4,2,1,5,7,6,8]
	a = s.buildTree(P,I)

	L = [a]
	while len(L) != 0:
		if L[0].left != None:
			L.append(L[0].left)
		if L[0].right != None:
			L.append(L[0].right)
		print L[0].val
		L.remove(L[0])

