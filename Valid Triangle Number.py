class Solution(object):
	# def triangleNumber(self, nums):
	# 	"""
	# 	:type nums: List[int]
	# 	:rtype: int
	# 	"""
	# 	nums.sort()
	# 	number = 0
	# 	length = len(nums)
	# 	start = 0
	# 	for x in xrange(length - 2):
	# 		start = x + 2
	# 		# print '     set_stat',start
	# 		for y in xrange(x + 1, length - 1):
	# 			start = max(start, y+1)
	# 			z_num = self.calc_z_num(nums, x, y, start, length-1)
	# 			number += z_num + start - y - 1
	# 			start += z_num
	# 			# print '         n',number,x,y,z_num,start

	# 	return number

	# def calc_z_num(self, nums, x, y, start, end):
	# 	if start > end:
	# 		return 0

	# 	if start == end:
	# 		return self.is_triangle(nums[x], nums[y], nums[start])

	# 	v1 = self.is_triangle(nums[x], nums[y], nums[start])
	# 	v2 = self.is_triangle(nums[x], nums[y], nums[end])
	# 	if v1 and v2:
	# 		return end - start + 1
	# 	if not v1 and not v2:
	# 		return 0

	# 	return self.calc_z_num(nums, x, y, start + 1, (start + end) / 2) + self.calc_z_num(nums, x, y, (start + end) / 2 + 1, end - 1) + v1 + v2

	# def is_triangle(self, x, y, z):
	# 	return x + y > z and y + z > x and x + z > y

	def triangleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.sort()
		number = 0
		for z in xrange(2,len(nums)):
			x = 0
			y = z - 1
			while x < y:
				if nums[x] + nums[y] > nums[z]:
					number += y - x
					y -= 1
				else:
					x += 1

		return number
		
if __name__ == '__main__':
	s = Solution()
	# print s.triangleNumber([0,0,1,1])
	print s.triangleNumber([2,2,3,4])
	print s.triangleNumber([60,94,18,81,97,83,70,100,11,24,7,90,40,41,41,56,83,67,74,64,52,91,45,60,54,41,85,63,78,31,7,41,96,74,10,43,39,98,60,47,49,58,36,27,21,69,100,3,84,64,5,15,97,48,80,43,67,81,88,78,80,85,77,28,34,65,77,56,64,89,75,62,29,74,6,91,42,50,26,54,14,12,88,4,56,84,3,24,33,95,82,57,19,54,31,53,63,23,23,75])
	print s.triangleNumber([15,44,16,43,47,47,45,27,46,2,28,12,49,22,36,12,6,48,28,19,18,34,46,38,42,3,21,3,54,35,21,54,13,46,50,23,53,43,5,48,40,48,10,31,15,35,50,8,48,55,52,18,54,16,35,4,43,55,34,13,5,13,27,41,19,22,21,26,48,4,15,1,45,51,13,49,22,33,18,18,52,27,6,41,7,11,48,17,37,31,42,3,45,22,6,45,42,5,28,39,35,30,24,21,49,49,47,54,28,42,40,26,47,8,28,1,44,4,45,23,49,53,12,48,16,27,36,21,18,41,43,9,55,27,37,41,5,43,12,45,0,34,19,48,14,22,43,14,13,38,15,7,41,8,37,13,45,31,47,38,45,38,50,44,20,40,39,38,26,29,24,10,30,23,53,38,39,3,37,4,15,22,29,4,5,4,4,19,35,30,30,49,16,32,36,26,37,53,46,28,24,13,12,29,2,36,21,19,15,11,22,10,30,29,40,14,17,39,36,17,23,39,13,29,51,8,55,10,10,47,39,1,46,27,18,7,49,38,27,14,26,35,5,46,54,12,18,30,11,6,29,52,44,38,51,22,26,24,41,13,39,27,0,36,38,7,37,7,9,25,4,8,52,33,46,33,42,43,17,23,20,23,41,8,47,16,48,46,35,35,24,0,17,12,40,52,11,16,7,33,6,21,30,32,55,52,52,28,11,35,39,15,27,47,52,0,11,41,50,10,13,10,5,40,21,0,27,12,39,20,27,39,19,28,5,51,45,19,3,1,15,53,31,45,36,33,22,4,22,20,3])