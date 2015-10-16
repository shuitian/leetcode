"""class Solution(object):
	def FindZero(self, matrix):
		for x in xrange(0,len(matrix)):
			for y in xrange(0,len(matrix[x])):
				if matrix[x][y] == 0:
					self.tx = x
					return [x,y]
		return [-1,-1]
				
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		for x in xrange(0,len(matrix)):
			[row, col] = self.FindZero(matrix)
			if [row,col] == [-1,-1]:
				continue
			else :
				y = col
				print x,y,matrix
				if matrix[x][y] == 0:
					for i in xrange(0,x):
						matrix[i][y] = 0
					for i in xrange(0,len(matrix[x])):
						if i == y:
							continue
						elif matrix[x][i] == 0:
							self.recursion(matrix, x, i)
							break
						else :
							matrix[x][i] = 0
					for i in xrange(0,len(matrix)):
						[row, col] = self.FindZero(matrix)
						if [row,col] == [-1,-1]:
							continue
						else :
							y = col
							self.recursion(matrix, row, y)
							break
					for i in xrange(x,len(matrix)):
						matrix[i][y] = 0
					break
							
	def recursion(self, matrix, row, col):
		for i in xrange(0,row):
			matrix[i][col] = 0
		for i in xrange(col+1,len(matrix[row])):
			if matrix[row][i] == 0:
				self.recursion(matrix, row, col)
			else :
				matrix[x][i] = 0


if __name__ == '__main__':
	s = Solution()
	matrix = [[1,2,3],[4,0,6],[7,8,9]]
	print matrix
	s.setZeroes(matrix)
	print matrix"""