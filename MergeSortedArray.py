class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		pc = 0
		pb = 0
		pa  = 0
		C = A[:]
		while pa<m+n:
			# print(A,C)
			if pc>=m:
				A[pa] = B[pb]
				pa=pa+1
				pb=pb+1
			elif pb>=n:
				A[pa] = C[pc]
				pa=pa+1
				pc=pc+1
			else:
				if C[pc]<=B[pb]:
					A[pa] = C[pc]
					pa=pa+1
					pc=pc+1
				else:
					A[pa] = B[pb]
					pa=pa+1
					pb=pb+1	

if __name__ == '__main__':
	s = Solution()
	a = [1,2,6,0,0,0,0,0,0,0]
	b = []
	s.merge(a,3,b,0)
	print(a)
