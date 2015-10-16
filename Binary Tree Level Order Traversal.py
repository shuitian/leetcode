class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if root == None :
			return []
		queue = [root,None]
		ret = []
		row = []
		while len(queue)>1:
			#print queue
			front = queue[0]
			if front == None:
				ret.append(row)
				row = []
				del queue[0]
				queue.append(None)
			else :
				row.append(front.val)
				if front.left!=None:
					queue.append(front.left)
				if front.right!=None:
					queue.append(front.right)
				del queue[0]
		ret.append(row)
		return ret



if __name__ == '__main__':
	s = Solution()
	r1 = TreeNode(1)
	r2 = TreeNode(2)
	r3 = TreeNode(3)
	r4 = TreeNode(4)
	r5 = TreeNode(5)
	r6 = TreeNode(6)
	r7 = TreeNode(7)
	r1.left = r2;
	r1.right = r3;
	r2.left = r4;
	r4.right = r7
	r3.right = r5;	
	r5.right = r6;
	print s.levelOrder(None)