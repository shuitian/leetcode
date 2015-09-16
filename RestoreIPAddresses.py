class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		m = []
		l = len(s)
		for a in xrange(1, l-2):
			ip1 = int(s[:a])
			if ip1>255 or (s[0]=='0' and a-0 > 1):
				continue
			for b in xrange(a+1, l-1):
				ip2 = int(s[a:b])
				if ip2>255 or (s[a]=='0' and b-a >1):
					continue
				for c in xrange(b+1, l):
					ip3 = int(s[b:c])
					if ip3>255 or (s[b]=='0' and c-b > 1):
						continue
					ip4 = int(s[c:l])
					if ip4>255 or (s[c]=='0' and l -c > 1):
						continue
					r = str(ip1)+'.'+str(ip2)+'.'+str(ip3)+'.'+str(ip4)
					m.append(r)
		return m


if __name__ == '__main__':
	s = Solution()
	print s.restoreIpAddresses("0000")