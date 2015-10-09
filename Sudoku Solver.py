class Solution(object):
	def initHashTable(self, board, hashtable):
		for x in xrange(0,len(board)):
			for y in xrange(0,len(board[x])):
				if board[x][y]!= '.':
					if self.IsHashCollision(hashtable, x, y, board[x][y]):
						return False
					else:
						self.AddIntoHashTable(hashtable, x, y, board[x][y])

	def IsHashCollision(self, hashtable, x, y, value):
		if hashtable[x].has_key(value):
			return True
		if hashtable[9+y].has_key(value):
			return True
		if hashtable[18+x/3*3+y/3].has_key(value):
			return True
		return False

	def AddIntoHashTable(self, hashtable, x, y, value):
		hashtable[x][value] = 1
		hashtable[9+y][value] = 1
		hashtable[18+x/3*3+y/3][value] = 1

	def DelFromHashTable(self, hashtable, x, y, value):
		del hashtable[x][value]
		del hashtable[9+y][value]
		del hashtable[18+x/3*3+y/3][value]

	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		hashtable = [{} for x in xrange(0,27)]
		self.initHashTable(board, hashtable)
		self.TraceBack(hashtable,board)
	
	def FindPlace(self, board):
		for x in xrange(0,9):
			for y in xrange(0,9):
				if board[x][y] == '.':
					return [x,y]
		return [10,10]		

	def TraceBack(self, hashtable, board):
		[x,y] = self.FindPlace(board)
		if [x,y] == [10,10]:
			return True
		for z in "123456789":
			if self.IsHashCollision(hashtable, x, y, z):
				continue
			else :
				board[x] = board[x][0:y] + z + board[x][y+1:]
				self.AddIntoHashTable(hashtable, x, y, z)
				#print "***%r***"%(board[x])
				if self.TraceBack(hashtable, board):
					return True
				board[x] = board[x][0:y] + '.' + board[x][y+1:]
				self.DelFromHashTable(hashtable, x, y, z)
		if board[x][y] == '.':
			return False
					
if __name__ == '__main__':
	s = Solution()
	board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
	#board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
	print board
	s.solveSudoku(board)
	print board