class Solution(object):
	lambda_data = [
		lambda x,y:x+y,
		lambda x,y:x-y,
		lambda x,y:y-x,
		lambda x,y:x*y,
		lambda x,y:float(x)/y if y else None,
		lambda x,y:float(y)/x if x else None,
	]
	def judgePoint24(self, nums, index = 0):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		# print index*'\t','nums',nums
		if len(nums) == 1:
			return abs(nums[0] - 24) < 0.001

		for x in xrange(len(nums)):
			num1 = nums[x]
			for y in xrange(x + 1, len(nums)):
				num2 = nums[y]
				# print '    1',num1,num2
				for _lambda in Solution.lambda_data:
	
					del nums[x]
					del nums[y-1]
					new_number = _lambda(num1, num2)
					nums.append(new_number)
					if new_number is not None and self.judgePoint24(nums, index+1):
						return True

					nums.pop(-1)
					nums.insert(y-1, num2)
					nums.insert(x, num1)
		return False

if __name__ == '__main__':
	s = Solution()
	# print s.judgePoint24([4,6])
	# print s.judgePoint24([4,1,8,7])
	# print s.judgePoint24([1,2,1,2])
	print s.judgePoint24([3,3,8,8])
	# print s.judgePoint24([1,2,3,4])