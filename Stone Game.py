class Solution(object):
	def stoneGame(self, piles):
		"""
		:type piles: List[int]
		:rtype: bool
		"""
		# 只要和为奇数，就恒为true，先手必赢
		return True

		number = len(piles)
		dp = [[None for x in xrange(number)] for x in xrange(number)]
		for x in xrange(number):
				dp[x][x] = -piles[x]
		for i in xrange(number):
			for x in xrange(number - i):
				if i == 0:
					dp[x][x + i] = piles[x]
				else:
					dp[x][x + i] = max(piles[x] - dp[x + 1][x + i], piles[x + i] - dp[x][x + i - 1])
		# print dp
		return dp[0][-1] > 0

		
if __name__ == '__main__':
	s = Solution()
	print s.stoneGame([1,3,3,4,2,1])