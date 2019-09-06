class Solution(object):

	def setup_from_data(self, tickets):
		from_data = {}
		for ticket in tickets:
			_from, to = ticket
			from_data.setdefault(_from, []).append(to)
		for ports in from_data.itervalues():
			ports.sort()
		# print from_data
		return from_data

	def findItinerary(self, tickets):
		"""
		:type tickets: List[List[str]]
		:rtype: List[str]
		"""
		from_data = self.setup_from_data(tickets)
		return self._findItinerary(from_data, ["JFK"])

	def _findItinerary(self, from_data, pre_ports):
		# print 111,pre_ports,from_data
		if not from_data:
			return pre_ports
		start_port = pre_ports[-1]
		if start_port not in from_data:
			return

		ports = from_data[start_port]
		for index, next_port in enumerate(ports[:]):
			# print 'start',from_data[start_port],ports
			del from_data[start_port][index]
			if not from_data[start_port]:
				del from_data[start_port]
			pre_ports.append(next_port)
			ret = self._findItinerary(from_data, pre_ports)
			if ret:
				return ret

			pre_ports.pop(-1)
			from_data.setdefault(start_port,[]).insert(index, next_port)
			# print 'end',from_data[start_port],ports

if __name__ == '__main__':
	s = Solution()

	# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
	# print s.findItinerary(tickets)

	tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
	print s.findItinerary(tickets)

	# tickets = [["MEL","PER"],["SYD","CBR"],["AUA","DRW"],["JFK","EZE"],["PER","AXA"],["DRW","AUA"],["EZE","SYD"],["AUA","MEL"],["DRW","AUA"],["PER","ANU"],["CBR","EZE"],["EZE","PER"],["MEL","EZE"],["EZE","MEL"],["EZE","TBI"],["ADL","DRW"],["ANU","EZE"],["AXA","ADL"]]
	# print s.findItinerary(tickets)	