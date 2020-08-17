# -*- coding:utf-8 -*-

class Solution(object):

	def setup_jump_data(self, arr, d, arr_start_index, arr_length):
		if not arr:
			return

		max_value = max(arr)
		max_index = arr.index(max_value)
		right = arr[max_index+1:max_index+1+d]
		if right:
			right_max = max(right)
			if right_max >= max_value:
				right_max_index = right.index(right_max)
			else:
				right_max_index = d
		else:
			right_max_index = 0
		self.jump_data[max_index + arr_start_index] = (arr_start_index + max(max_index - d, 0), arr_start_index + min(max_index + right_max_index, min(len(arr) - 1, arr_length - 1)))
		self.setup_jump_data(arr[:max_index], d, arr_start_index, arr_length)
		self.setup_jump_data(arr[max_index+1:], d, arr_start_index + max_index + 1, arr_length)

	def maxJumps(self, arr, d):
		"""
		:type arr: List[int]
		:type d: int
		:rtype: int
		"""
		self.jump_data = {}
		self.setup_jump_data(arr, d, 0, len(arr))

		self.visit_time_data = {}
		max_visit_time = None
		for i, x in enumerate(arr):
			visit_time = self.get_visit_time(i, d, arr)
			max_visit_time = max(max_visit_time, visit_time)
		return max_visit_time

	def get_visit_time(self, i, d, arr):
		if i in self.visit_time_data:
			return self.visit_time_data[i]

		if i not in self.jump_data:
			return 1
		
		start, end = self.jump_data[i]
		max_visit_time = None
		for j in xrange(max(i-d, 0), i):
			if start <= j <= end:
				visit_time = self.get_visit_time(j, d, arr) + 1
				max_visit_time = max(max_visit_time, visit_time)
				
		for j in xrange(min(len(arr), i+1), min(len(arr), i + d + 1)):
			if start <= j <= end:
				visit_time = self.get_visit_time(j, d, arr) + 1
				max_visit_time = max(max_visit_time, visit_time)

		self.visit_time_data[i] = max_visit_time or 1
		return self.visit_time_data[i]
		
if __name__ == '__main__':
	s = Solution()
	print s.maxJumps([3,3,3,3,3], 3),1,s.jump_data,s.visit_time_data
	print s.maxJumps([7,6,5,4,3,2,1], 1),7,s.jump_data,s.visit_time_data
	print s.maxJumps([7,1,7,1,7,1], 2),2,s.jump_data,s.visit_time_data
	print s.maxJumps([6,4,14,6,8,13,9,7,10,6,12], 2),4,s.jump_data,s.visit_time_data
	print s.maxJumps([66], 1),1,s.jump_data,s.visit_time_data
	l = [20,2,35,89,46,72,68,89,93,35,37,88,26,33,60,14,49,19,37,96,20,71,21,33,11,75,52,32,53,50,33,34,66,24,41,56,15,35,93,94,95,96,40,92,4,44,28,50,55,68,50,47,19,47,43,100,96,43,58,88,58,29,34,78,78,21,5,67,80,79,69,79,51,41,58,95,55,71,48,68,87,96,44,90,74,68,43,77,54,50,29,43,78,1,36,84,76,79,47,52,61,74,60,7,27,33,17,8,16,56,98,70,6,14,4,54,55,27,95,56,51,50,58,63,60,35,44,54,82,20,24,37,78,14,5,51,99,40,40,8,96,30,68,75,98,47,16,37,65,17,61,36,1,83,40,72,88,94,92,63,39,76,91,5,95,98,94,20,23,89,44,31,87,71,79,51,100,42,72,75,4,17,62,47,74]
	print s.maxJumps(l, 67),14,s.jump_data,s.visit_time_data