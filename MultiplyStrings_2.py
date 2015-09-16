class Solution:
	# @param num1, a string
	# @param num2, a string
	# @return a string
	def multiply(self, num1, num2):
		a = int(num1)
		b = int(num2)
		return str(a*b)


if __name__ == '__main__':
	s = Solution()
	a = s.multiply("123", "456")
	print "%r"%a