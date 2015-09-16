# Definition for an interval.
class Interval(object):
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution(object):
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)
		self.sort(intervals)

		end = -1
		for x in xrange(0, len(intervals)):
			while x < len(intervals) and intervals[x].start <= end :
				if intervals[x].end >= end:
					intervals[x-1].end = intervals[x].end
					end = intervals[x].end
				intervals.remove(intervals[x])
			if x >= len(intervals)-1:
				break
			end = intervals[x].end
		return intervals

	def sort(self, intervals):
		s = []
		for x in intervals:
			s.append([x.start, x.end])
		s= sorted(s)
		for x in xrange(0, len(intervals)):
			intervals[x].start = s[x][0]
			intervals[x].end = s[x][1]



if __name__ == '__main__':
	a = []
	# for x in xrange(1,100,10):
	a.append(Interval(1, 5))
	a.append(Interval(6, 7))
	a.append(Interval(8, 9))
	solution = Solution();
	intervals =  solution.insert(a, Interval(5,123))
	for x in intervals:
		print x.start,x.end
