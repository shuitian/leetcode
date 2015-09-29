class Solution(object):
	def maxProfit_1(self, prices):#Best Time to Buy and Sell Stock
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

	def resetPrices(self, prices):
		min = prices[0]
		max = prices[0]
		stage = []
		flag = False
		for x in prices:
			if x < max:
				if flag:
					stage.append(min)
					stage.append(max)
					flag = False
				min = x
				max = x
			elif x > max:
				max = x
				flag = True
		if max >min:
			stage.append(min)
			stage.append(max)
		return stage

	def maxProfit(self, prices):#Best Time to Buy and Sell Stock III
		if len(prices) == 0:
			return 0
		prices = self.resetPrices(prices)
		#length = len(prices)/2
		#print prices
		return self.sub_maxProfit(prices)
		
	def sub_maxProfit(self, prices):
		l = len(prices)
		if l == 0:
			return 0
		elif l == 2:
			return prices[1]-prices[0]
		else :
			max = 0
			for x in xrange(1,l/2):
				profit = self.maxProfit_1(prices[0:2*x])+self.maxProfit_1(prices[2*x:l])
				if profit>max :
					max = profit
		return max



		



if __name__ == '__main__':
	s = Solution()
	prices = [123,43,13,45,13,465,435,132,65,3,435,4,13,16,468435,151,564,165,4654,35,135,43,5435,435,135,468,468,13,5135,13]
	p1 = [1,100,2,3,400,1,6,55,55,4,3,2,3,1000]
	p2 = [1,100]
	#print s.maxProfit(prices)
	#print s.maxProfit(p1)
	print s.maxProfit(p2)
