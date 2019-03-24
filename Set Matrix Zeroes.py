class Solution(object):
	def setZeroes(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		self.rows = []
		self.cols = []
		for x in xrange(len(matrix)):
			for y in xrange(len(matrix[x])):
				if matrix[x][y] == 0:
					self.set_row(x)
					self.set_col(y)

		for row in self.rows:
			matrix[row] = [0] * len(matrix[0])

		for col in self.cols:
			for x in matrix:
				x[col] = 0

	def set_row(self, row):
		self.rows.append(row)

	def set_col(self, col):
		self.cols.append(col)

if __name__ == '__main__':
	s = Solution()
	matrix = [[1,2,3],[4,0,6],[7,8,9]]
	print matrix
	s.setZeroes(matrix)
	print matrix