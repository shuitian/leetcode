class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	# def __init__(self):
	# 	super(ClassName, self).__init__()


	def canCompleteCircuit(self, gas, cost):
		number = len(gas)
		i = 0
		j = 0
		k = number-1
		sum =0
		while j<=k:
			sum = sum+gas[j]-cost[j]
			j = j+1
			while sum<0 and j<=k:
				sum = sum+gas[k]-cost[k]
				k = k-1

		if sum<0:
			return -1
		else:
			return (k+1)%number

def main():
	t = int(raw_input())
	gas = []
	cost = []
	for x in xrange(0,t):
		g,c = raw_input().split(' ')
		gas.append(int(g))
		cost.append(int(c))
	a = Solution()
	print a.canCompleteCircuit(gas,cost)

if __name__ == '__main__':
	main()
