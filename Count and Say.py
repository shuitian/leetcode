# -*- coding:utf-8 -*-

class Solution(object):
	save_strs = []

	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""

		s = '1'
		for x in xrange(n-1):
			s = self.say_str(x, s)
		return s

	def say_str(self, x, s):
		if x < len(Solution.save_strs):
			return Solution.save_strs[x]
		
		new_str = ''
		number = 0
		char = s[0]
		for c in s:
			if c == char:
				number += 1
			else:
				new_str += str(number) + char
				char = c
				number = 1
		new_str += str(number) + c

		Solution.save_strs.append(new_str)
		return new_str

if __name__ == '__main__':
	s = Solution()
	print s.countAndSay(30)
	print s.countAndSay(1)
	print s.countAndSay(2)
	print s.countAndSay(3)
	print s.countAndSay(4)
	print s.countAndSay(5)