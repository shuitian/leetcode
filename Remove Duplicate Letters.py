# -*- coding: utf-8 -*-

class Solution(object):

	def removeDuplicateLetters(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		index = self.get_first_end_index(s)
		if index is None:
			return ''

		min_sub_list, new_begin = self.get_min_sub_str(s[:index+1])
		_sub1 = ''.join(min_sub_list) + s[index]
		s = ''.join([c for i,c in enumerate(s) if i >= new_begin and c not in _sub1])
		_sub2 = self.removeDuplicateLetters(s)
		return _sub1 + _sub2
	
	def append_to_list(self, min_sub_list, new_char):
		while min_sub_list:
			last = min_sub_list[-1]
			if new_char > last:
				min_sub_list.append(new_char)
				return

			min_sub_list.pop()
		if not min_sub_list:
			min_sub_list.append(new_char)

	def get_min_sub_str(self, s):
		max_char = s[-1]
		min_sub_list = []
		new_begin = None
		for index,c in enumerate(s): 
			if c == max_char and new_begin is None:
				new_begin = index
				continue
			if c >= max_char:
				continue
			if c in min_sub_list:
				continue

			new_begin = None
			self.append_to_list(min_sub_list, c)

		return min_sub_list, new_begin

	def get_first_end_index(self, s):
		if not s:
			return None
		number_dict = {c: index for index, c in enumerate(s)}
		return min(number_dict.values())

	# def removeDuplicateLetters(self, s):
	# 	rindex = {c: i for i, c in enumerate(s)}
	# 	result = ''
	# 	for i, c in enumerate(s):
	# 		if c not in result:
	# 			while c < result[-1:] and i < rindex[result[-1]]:
	# 				result = result[:-1]
	# 			result += c
	# 	return result

if __name__ == '__main__':
	s = Solution()
	# print s.removeDuplicateLetters('abacb')
	# print s.removeDuplicateLetters('bcabcccc')
	# print s.removeDuplicateLetters('cbacdcbc')
	# print s.removeDuplicateLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws")
	print s.removeDuplicateLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws") == 'bfegkuyjorndiqszpcaw'
	print s.removeDuplicateLetters('yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk')
	# print s.removeDuplicateLetters("yioccqiorhtoslwlvfgzycahonecugtatbyphpuunwvaalcpndabyldkdtzfjlgwqk") == "ciorhsaebpunvdyktzfjlgwq"
	# print s.removeDuplicateLetters("eywdgenmcnzhztolafcfnirfpuxmfcenlppegrcalgxjlajxmphwidqqtrqnmmbssotoywfrtylm")
	# print s.removeDuplicateLetters("wmxkuuoordmnpnebikzzujdpscpedcrsjphcaykjsmobturjjxxpoxvvrynmapegvtlasmyuddgxygkaztmbpkrnukbxityz")
