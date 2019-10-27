# leetcode 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res, d = [], {}
        for i,x in enumerate(nums):
            d[x] = i
        for i,a in enumerate(nums):
            b = target - a
            if b in d and d[b] != i:
                return [i, d[b]]
        return None
    

s = Solution()
print(s.twoSum([2,7,11,15,3,3], 6))