# -*- coding:utf-8 -*-

class Solution(object):
	def getKth(self, lo, hi, k):
		"""
		:type lo: int
		:type hi: int
		:type k: int
		:rtype: int
		"""
		d = {}
		l = []
		for x in xrange(lo, hi + 1):
			self.calc_power(d, l, lo, hi, x)
		l.sort()
		return l[k-1][1]

	def calc_power(self, d, l, lo, hi, key):
		# print '			k',d,key
		if key in d:
			return d[key]
		if key == 1:
			value = 0
			d[key] = value
			if lo <= key <= hi:
				l.append((value, key))
			return value
		if key%2 == 0:
			value = self.calc_power(d, l, lo, hi, key/2) + 1
			d[key] = value
			if lo <= key <= hi:
				l.append((value, key))
			return value
		else:
			value = self.calc_power(d, l, lo, hi, key*3+1) + 1
			d[key] = value
			if lo <= key <= hi:
				l.append((value, key))
			return value

if __name__ == '__main__':
	s = Solution()
	print s.getKth(12, 15, 2)
	print s.getKth(1, 1, 1)
	print s.getKth(7, 11, 4)
	print s.getKth(10, 20, 5)
	print s.getKth(1, 1000, 777)