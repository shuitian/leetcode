class Solution(object):
	def findMinDifference(self, timePoints):
		"""
		:type timePoints: List[str]
		:rtype: int
		"""
		timePoints = sorted([int(t[:2]) * 60 + int(t[-2:]) for t in timePoints])
		length = len(timePoints)
		timePoints.append(timePoints[0])
		min_second_diff = min([720 - abs(abs(timePoints[x] - timePoints[(x+1)%length]) - 720) for x in xrange(length)])
		return min_second_diff

if __name__ == '__main__':
	s = Solution()
	print s.findMinDifference(['00:00','23:58','14:01','13:58'])