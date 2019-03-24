# -*- coding:utf-8 -*-

class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x == 0:
			return 0

		floor = -2**31
		ceiling = 2**31 - 1
		r = self.reverse_unsigned(x * (1 if x > 0 else (-1)))
		r *= 1 if x > 0 else -1
		if r < floor:
			return 0
		if r > ceiling:
			return 0
		return r

	def reverse_unsigned(self, x):
		ret = 0
		while x:
			ret = ret * 10 + x % 10
			x = x / 10
		return ret

if __name__ == '__main__':
	s = Solution()
	print s.reverse(123)
	print s.reverse(-120)
	print s.reverse(-123)
	print s.reverse(1534236469)