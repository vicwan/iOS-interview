# leetcode 239. Sliding Window Maximum

import collections

class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		if not nums:
			return None
		res, window = [], []
		# window 中存储的是 nums 的下标，并非元素本身
		for i, x in enumerate(nums):
			if i >= k and window[0] <= i - k:
				window.pop(0)
			while window and nums[window[-1]] <= x:
				window.pop()
			window.append(i)
			if i >= k - 1:
				res.append(nums[window[0]])
		return res
		
s = Solution()
#print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.maxSlidingWindow([1,3,1,2,0,5], 3))
