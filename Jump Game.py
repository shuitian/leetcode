class Solution(object):
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		max = 0
		for x in xrange(0, len(nums)):
			if x > max :
				return False
			step = x + nums[x]
			if step > max:
				max = step
			if step >= len(nums)-1:
				return True
		return False

if __name__ == '__main__':
	s = Solution()
	nums = [3,2,1,0,4]
	nums = [3,2,1,1,4]
	nums = [1]
	nums = [0]
	nums = [0,0]
	nums = [1,0]
	nums = [2,0]
	nums = [1,0,1]
	nums = [1,1,1]
	print s.canJump(nums)