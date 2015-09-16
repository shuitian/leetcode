class Solution(object):
	def __init__(self):
		super(Solution, self).__init__()

	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		num_sorted = sorted(num)
		# print num_sorted
		# print target
		begin = 0
		end = len(num)-1
		while ((num_sorted[begin]+num_sorted[end]) != target) and (begin < end):
			# print begin,end,num_sorted[begin],num_sorted[end]
			if num_sorted[begin]+num_sorted[end] >target:
				end = end-1
			elif num_sorted[begin] + num_sorted[end] <target:
				begin = begin +1

		# print begin,end,num_sorted[begin],num_sorted[end]
		ret1 = num.index(num_sorted[begin])+1
		del num[ret1-1]
		ret2 = num.index(num_sorted[end])+1
		if ret1<ret2:
			ret2= ret2+1
		else:
			ret = ret1
			ret1 = ret2
			ret2 = ret
		return (ret1,ret2)

def main():
	while True:
		number, target = raw_input().split(' ')
		# print number, target
		
		
		numbers = raw_input().split(' ')
		for x in xrange(0, len(numbers)):
			numbers[x]= int(numbers[x])
		a = Solution()
		print a.twoSum(numbers,int(target))
	

if __name__ == '__main__':
	main()