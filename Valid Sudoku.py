class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		hashtable = [{} for x in xrange(0,27)]
		for x in xrange(0,len(board)):
			for y in xrange(0,len(board[x])):
				#print board[x][y],x,y
				if board[x][y]!= '.':
					if hashtable[x].has_key(board[x][y]):
						return False
					else:
						hashtable[x][board[x][y]] = 1
					if hashtable[9+y].has_key(board[x][y]):
						return False
					else:
						hashtable[9+y][board[x][y]] = 1
					if hashtable[18+x/3*3+y/3].has_key(board[x][y]):
						return False
					else:
						hashtable[18+x/3*3+y/3][board[x][y]] = 1
		return True

if __name__ == '__main__':
	s = Solution()
	board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
	#board = ["53..7....","6..195...",".98....6.","8...6...3","4..8.3..1","7...2...6",".6....28.","...419..5","....8..79"]
	print s.isValidSudoku(board)