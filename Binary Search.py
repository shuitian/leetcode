class Solution(object):
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		start = 0
		end = len(nums) - 1
		while start <= end:
			middle = (start + end) /2
			v_middle = nums[middle]

			if v_middle == target:
				return middle

			if v_middle < target:
				start = middle + 1
			else:
				end = middle - 1
		return -1

if __name__ == '__main__':
	s = Solution()
	print s.search(range(10),8)
	print s.search(range(10),12)
	print s.search([12],12)
	print s.search([],12)