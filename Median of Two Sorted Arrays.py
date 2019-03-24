class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		nums1.extend(nums2)
		nums1.sort()
		l = len(nums1)
		return (nums1[l/2] + nums1[(l-1)/2]) / 2.0
		
if __name__ == '__main__':
	s = Solution()
	print s.findMedianSortedArrays([1,3],[2])
	print s.findMedianSortedArrays([1,2],[3,4])