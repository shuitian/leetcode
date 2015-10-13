class Solution(object):
	def jump(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 1:
			return 0
		min = 0
		max = 0
		times = 0
		while(True):
			times +=1
			flag = True
			for x in xrange(min,max+1):
				if flag:
					min = max+1
					flag = False
				step = x + nums[x]
				if step > max:
					max = step
				if step >= len(nums)-1:
					return times
			if min == max +1:
				break
		return -1

if __name__ == '__main__':
	s = Solution()
	nums = [3,2,1,0,4]
	nums = [3,2,1,1,4]
	#nums = [1]
	#nums = [0]
	#nums = [0,0]
	#nums = [1,0]
	#nums = [2,0]
	#nums = [1,0,1]
	#nums = [1,2,1,1]
	print s.jump(nums)
		