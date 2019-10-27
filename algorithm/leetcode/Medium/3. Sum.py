#leetcode 15. 3Sum

# Using hash map
#class Solution(object):
#    def threeSum(self, nums):
#        """
#        :type nums: List[int]
#        :rtype: List[List[int]]
#        """
#        if len(nums) < 3:
#            return []
#        res = set()
#        m = {}
#        for i, x in enumerate(nums):
#            m[x] = i
#        for i, a in enumerate(nums):
#            #first num a
#            for j, b in enumerate(nums):
#                if i is j:
#                    continue
#                c = -a - b
#                if c in m and i != m[c] and j != m[c]:
#                    res.add(tuple(sorted([a,b,c])))
#        return map(list, res)
    

# Using two pointers
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and  nums[i] == nums[i - 1]: #注意，去重的要点
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    #注意，去重的要点
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1; right -= 1
        return res
                
            
    
s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
