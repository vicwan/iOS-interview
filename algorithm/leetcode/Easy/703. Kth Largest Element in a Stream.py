# leetcode 703. Kth Largest Element in a Stream

import heapq

class KthLargest:

	def __init__(self, k, nums):
		"""
		:type k: int
		:type nums: List[int]
		"""
		#构建小顶堆，注意未满的情况
		self.k = k
		self.bigKs = nums
		heapq.heapify(self.bigKs)
		while len(self.bigKs) > k:
			heapq.heappop(self.bigKs)

	def add(self, val):
		"""
		:type val: int
		:rtype: int
		"""
		if len(self.bigKs) < self.k:
			heapq.heappush(self.bigKs, val)
		else:
			heapq.heappushpop(self.bigKs, val)
		return self.bigKs[0]

# Test
a = KthLargest(3, [4,5,8,2])
print(a.add(3)) 	# 4
print(a.add(5)) 	# 5
print(a.add(10)) 	# 5
print(a.add(9)) 	# 8
print(a.add(4)) 	# 8

