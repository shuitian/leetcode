import copy
class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		super(Solution, self).__init__()

	def solveNQueens(self, n):
		self.list = []
		self.n = n
		self.a = [(['.']*n )for i in xrange(n)]
		self.row = [0]*n
		self.column = [0]*n
		self.left = [0]*(n*2-1)
		self.right = [0]*(n*2-1)

		self.DFS(0)
		for x in self.list:
			for i in xrange(0,len(x)):
				x[i] = ''.join(x[i])
		return  self.list


	def DFS(self, i):
		if i == self.n:
			self.list.append(copy.deepcopy(self.a))		
			return 0;
		for j in xrange(0,self.n):
			if self.isOccupied(i,j) == True:
				continue
			

			self.setOccupied(i,j)

			self.DFS(i + 1)

			self.resetOccupied(i,j)

	def isOccupied(self, i , j):
		if self.column[j] ==1:
			return True
		if self.left[i+j] == 1:
			return True
		if self.right[i-j+self.n-1] == 1:
			return True
		return False

	def setOccupied(self, i ,j):
		self.a[i][j] = 'Q'
		self.row[i] = 1
		self.column[j] = 1
		self.left[i+j] = 1
		self.right[i-j+self.n-1] = 1

	def resetOccupied(self, i ,j):
		self.a[i][j] = '.'
		self.row[i] = 0
		self.column[j] = 0
		self.left[i+j] = 0
		self.right[i-j+self.n-1] = 0
		
if __name__ == '__main__':
	a = Solution()
	print a.solveNQueens(4)
	print a.solveNQueens(3)
	print a.solveNQueens(5)
	print a.solveNQueens(6)