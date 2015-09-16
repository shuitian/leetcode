class Solution:
	# @return a boolean
	def isScramble(self, s1, s2):
		if self.check(s1,s2)== False:
			return False
		flag = False
		l = len(s1)
		if l == 1:
			if s1 == s2:
				return True;
			else: 
				return False;
		for x in xrange(1, l):
			Flag1 = self.isScramble(s1[:x],s2[:x]) and self.isScramble(s1[x:],s2[x:])
			# print s1[:x],s2[:x],s1[x:],s2[x:],"Flag1:",Flag1
			Flag2 = self.isScramble(s1[:x],s2[(l-x):]) and self.isScramble(s1[x:],s2[:(l-x)])
			# print s1[:x],s2[(l-x):],s1[(x:],s2[:(l-x)],"Flag2:",Flag2
			Flag = Flag1 or Flag2
			if Flag == True:
				return True
		return False

		
	def check(self, s1,s2):
		print s1,s2
		if len(s1) != len(s2):
			return False
		dict= {}
		for x in s1:
			if x in dict.keys():
				dict[x] = dict[x] +1
			else:
				dict[x] = 1
		for x in s2:
			if x in dict.keys():
				dict[x] = dict[x] -1
				if dict[x]<0:
					return False
			else:
				return False
		return True
				

if __name__ == '__main__':
	a = Solution()
	# print a.isScramble("great","rgtae") 
	# print a.isScramble("gr","rg") 
	# print a.isScramble("abcd","bdac") 
	# print a.isScramble("abc","bca") 
	print a.isScramble("a","a") 