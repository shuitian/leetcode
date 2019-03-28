# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
	def findSecretWord(self, wordlist, master):
		"""
		:type wordlist: List[Str]
		:type master: Master
		:rtype: None
		"""
		while wordlist:
			word = self.get_best_word(wordlist)
			ret = master.guess(word)
			if ret == 6:
				return 

			wordlist = [_word for _word in wordlist if sum([word[x] == _word[x] for x in xrange(6)]) == ret and word != _word]

	def get_best_word(self, wordlist):
		index_dict = {0:{},1:{},2:{},3:{},4:{},5:{}}
		for word in wordlist:
			for x in xrange(6):
				index_dict[x][word[x]] = index_dict[x].get(word[x], 0) + 1
		
		value_list = []
		for word in wordlist:
			value = 0
			for x in xrange(6):
				value += index_dict[x][word[x]]
			value_list.append((value, word))
		value_list.sort(reverse = True)
		return value_list[0][1]


if __name__ == '__main__':
	class Master(object):
		def __init__(self, wordlist, secret):
			self.wordlist = wordlist
			self.secret = secret
			self.guess_time = 0
			self.correst = False

		def pass_case(self):
			return self.guess_time <= 10 and self.correst

		def guess(self, word):
			"""
			:type word: str
			:rtype int
			"""
			self.guess_time += 1
			if word not in self.wordlist:
				return -1
			number = 0
			for index, c in enumerate(self.secret):
				number += c == word[index]
			if number == len(self.secret):
				self.correst = True
			return number

	import random
	s = Solution()

	def test():
		wordlist = [''.join([chr(random.choice(range(26)) + ord('a')) for i in xrange(6)]) for x in xrange(100)]

		master = Master(wordlist,random.choice(wordlist))
		s.findSecretWord(wordlist, master)
		assert master.pass_case(), master.guess_time

	test()

