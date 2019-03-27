class Solution(object):
	def smallestRepunitDivByK(self, k):
		"""
		:type K: int
		:rtype: int
		"""
		if not k&1:
			return -1

		if k % 10 == 5:
			return -1

		v = 1 % k
		for x in xrange(1,k+1):
			
			if not v:
				return x
			v = (v * 10 + 1) % k
		# proof
		raise # This line never executes

# Proof:
# It is obvious that if K is the multiple of 2 or multiple of 5, N is definitely not multiple of K because the ones digit of N is 1. Thus, return -1 for this case.

# If K is neither multiple of 2 nor multiple of 5, we have this theorem.

# Theorem: there must be one number from the K-long candidates list [1, 11, 111, ..., 111..111(with K ones)], which is the multiple of K.

# Why? Let's think in the opposite way. Is it possible that none of the K candidates is the multiple of K?

# If true, then the module of these K candidate numbers (mod K) must be in [1, .., K-1] (K-1 possible module values). Thus, there must be 2 candidate numbers with the same module. Let's denote these two numbers as N_i with i ones, and N_j with j ones and i<j.

# Thus N_j-N_i = 1111...1000...0 with (j-i) ones and i zeros. N_j-N_i = 111..11 (j-i ones) * 100000..000 (i zeros). We know that N_i and N_j have the same module of K. Then N_j-N_i is the multiple of K. However, 100000..000 (i zeros) does not contain any factors of K (K is neither multiple of 2 nor multiple of 5). Thus, 111..11 (j-i ones) is the multiple of K. This is contradictory to our assumption that all K candidates including 111..11 (j-i ones) are not multiple of K.

# Finally, we know that there is at least one number, from the first K candidates, which is the multiple of K.
		
if __name__ == '__main__':
	s = Solution()
	print s.smallestRepunitDivByK(1) == 1
	print s.smallestRepunitDivByK(2) == -1
	print s.smallestRepunitDivByK(3) == 3
	print s.smallestRepunitDivByK(4) == -1
	print s.smallestRepunitDivByK(4133)