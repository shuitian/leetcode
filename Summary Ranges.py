class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		if len(nums) == 0:
			return []
		elif len(nums) == 1:
			return ["%d"%nums[0]]
		ranges = []
		flag = True
		s = ""
		begin = 0
		for x in xrange(0,len(nums)):
			if flag:
				s = '%d'%nums[x]
				begin = nums[x]
				flag = False
			else :
				if nums[x] == nums[x-1] + 1:
					if x == len(nums)-1:
						ranges.append(s + '->%d'%nums[x])
					continue
				else :
					if nums[x-1] != begin:
						s = s + '->%d'%nums[x-1]
					ranges.append(s)
					s = '%d'%nums[x]
					begin = nums[x]
					if x == len(nums)-1:
						ranges.append(s)
		return ranges






if __name__ == '__main__':
	s = Solution()
	nums = [0,2,4,5,7,8,10,11,99,100]
	print s.summaryRanges(nums)