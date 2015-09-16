class Solution:
	# @param version1, a string
	# @param version2, a string
	# @return an integer
	def compareVersion(self, version1, version2):
		v1 = version1.split('.')
		v2 = version2.split('.')
		l1 = len(v1)
		l2 = len(v2)
		l = 0
		if l1>l2:
			l = l2
		else:
			l = l1
		for x in xrange(0,l):
			if int(v1[x])>int(v2[x]):
				return 1
			elif int(v1[x])<int(v2[x]):
				return -1
		if l1>l2:
			for x in xrange(l,l1):
				if(int(v1[x])!=0):
					return 1
			return 0
		elif l1<l2:
			for x in xrange(l,l2):
				if(int(v2[x])!=0):
					return -1
			return 0
		return 0

if __name__ == '__main__':
	s = Solution();
	print s.compareVersion("1","1.1")