#leetcode 169. Majority Element
"""
四种算法：
1. 暴力法：枚举每一个数的 count
2. map
3. sort 之后，记录每个数的 count
4. 分治法
"""
class Solution(object):
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numD = {}
        for i, x in enumerate(nums):
            numD[x] = numD.get(x, 0) + 1
            if (i+1) > (len(nums)/2):
                if numD[x] > len(nums)/2:
                    return x
        return None
        
    
    def majorityElement3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mc, c = 0, 0
        last = None
        for x in nums:
            if x is not last:
                last = x
                c = 0
            c += 1
            if c >= mc:
                mc = c
            if mc > len(nums) / 2:
                return last
        return None
        
    def majorityElement4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#        if len(nums) == 1:
#            return nums[0]
#        elif len(nums) == 0:
#            return None
#        mi = int(len(nums)/2)
#        l = nums[0:mi]
#        r = nums[mi: len(nums)]
#        left = self.majorityElement4(l)
#        right = self.majorityElement4(r)
#        if not left:
#            return right
#        if not right:
#            return left
#        return max(left, right)
        
        
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)


s = Solution()
print(s.majorityElement4([3,2,3,1,1,4,4,4,4,4,4,5,3]))