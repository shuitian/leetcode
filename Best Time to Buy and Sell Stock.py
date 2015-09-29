class Solution(object):
	def maxProfit(self, prices):
		if len(prices) == 0:
			return 0
		min = prices[0]
		profit = 0
		for x in prices:
			if x < min:
				min = x
			elif x > min + profit:
				profit = x - min
		return profit


if __name__ == '__main__':
	s = Solution()
	prices = [123,43,13,45,13,465,435,132,65,3,435,4,13,16,468435,151,564,165,4654,35,135,43,5435,435,135,468,468,13,5135,13,]
	p1 = [100,2,3,400,5,6,55,4,3,2,1]
	print s.maxProfit(prices)
	print s.maxProfit(p1)
