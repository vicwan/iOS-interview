#leetcode 122. Best Time to Buy and Sell Stock II

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = None
        profit = 0
        for i, x in enumerate(prices):
            if buy is None and i + 1 < len(prices) and prices[i] < prices[i + 1]:
                buy = x
            elif buy is not None and i + 1 < len(prices) and prices[i] > prices[i + 1]:
                profit += x - buy
                buy = None
        if buy is not None:
            profit += prices[-1] - buy
        return profit


s = Solution()
print(s.maxProfit([1,2,3,4,5]))
            