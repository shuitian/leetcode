class Solution(object):
	"""docstring for Solution"""
	def __init__(self):
		super(Solution, self).__init__()
	
	def romanToInt(self, s):
		sum = 0
		letter = {
			'I':1,
			'V':5,
			'X':10,
			'L':50,
			'C':100,
			'D':500,
			'M':1000
		}
		last = 5000
		for x in xrange(0,len(s)):
			if letter[s[x]] > last:
				sum = sum + letter[s[x]]-last-last
			else:
				sum = sum + letter[s[x]]
			last = letter[s[x]]
		return sum 

if __name__ == '__main__':
	a = Solution()
	print a.romanToInt("MMDCCLI")
	print a.romanToInt("CCCLXIX")
	print a.romanToInt("LXXX")
	print a.romanToInt("CDXLVIII")
	print a.romanToInt("VII")
	print a.romanToInt("II")
	print a.romanToInt("II")
	print a.romanToInt("XD")
	print a.romanToInt("CDLXL")
	
		