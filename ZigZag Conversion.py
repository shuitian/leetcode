class Solution(object):
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		if numRows <= 1:
			return s

		length = len(s)
		step = numRows * 2 - 2
		numbers = [x for x in xrange(0, length + step, step)]
		s1 = ''
		for x in xrange(numRows):
			for num in numbers:
				if x != 0 and x != numRows - 1:
					s1 += self.get_char(s, length, num - x)
				s1 += self.get_char(s, length, num + x)
				
		return s1

	def get_char(self, s, length, index):
		if index >= 0 and index <  length:
			return s[index]
		return ''
		
if __name__ == '__main__':
	s = Solution()
	print s.convert('PAYPALISHIRING', 1)
	print s.convert('PAYPALISHIRING', 3)
	print s.convert('PAYPALISHIRING', 4)
	print s.convert('ABCD', 3)