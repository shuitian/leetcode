class Solution:
	# @param num1, a string
	# @param num2, a string
	# @return a string
	def multiply(self, num1, num2):
		a = list(num1[::-1])
		b = list(num2[::-1])
		len1 = len(num1)
		len2 = len(num2)

		c = a+b
		for x in xrange(0, len(c)):
			c[x] = 0
		# print a,b,c
		for x in xrange(0, len1):
			flag  = 0
			for y in xrange(0, len2):
				result = c[x+y] +int(a[x])*int(b[y])+flag
				flag = result/10
				c[x+y] = result%10 
			if flag !=0  :
				c[x+y+1] = c[x+y+1]+flag
		for x in xrange(0, len(c)):
			c[x] = str(c[x])
		c = c[::-1]
		# print c
		while len(c)>1 and c[0]== '0':
			c.remove(c[0])
		return "".join(c)


if __name__ == '__main__':
	s = Solution()
	a = s.multiply("123", "456")
	print "%r"%a