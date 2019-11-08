#leetcode 50. Pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        x^n
        1. 正负情况
        2. x 为分数情况, n 为整数
        3. 处理溢出
        分治策略
        """
        return self.myPow_recursive(x, n)
        
    def myPow_recursive(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
        
    def myPow_interative(self, x, n):
        if n < 0:
            x = 1/x
            n = -n
        ret = 1
        while n:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1
        return ret
            


s = Solution()
print(s.myPow(2, 3))