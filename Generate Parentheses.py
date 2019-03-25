class Solution(object):
	def __init__(self):
		self.t_value = {} # number : list

	def generateParenthesis(self, n):
		if n in self.t_value:
			return self.t_value[n]

		value = self._generateParenthesis(n)
		self.t_value[n] = value
		return value

	def _generateParenthesis(self, n):
		if n <= 0:
			return ['']
		if n == 1:
			return ['()']
		
		l = []
		l2 = self.generateParenthesis(n-1)
		for s in l2:
			self.add_element(l, '(' + s + ')')

		for x in xrange(1,n):
			l1 = self.generateParenthesis(x)
			l2 = self.generateParenthesis(n-x)
			for s1 in l1:
				for s2 in l2:
					self.add_element(l, s1+s2)
		return l

	def add_element(self, l, _str):
		if _str not in l:
			l.append(_str)

if __name__ == '__main__':
	s = Solution()
	print s.generateParenthesis(3)
	print s.generateParenthesis(4)

