# leetcode 22. Generate Parentheses

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        右括号不能比左括号多
        """
        self.ret = []
        self._gen(0, 0, n, "")
        return self.ret
        
    def _gen(self, l, r, n, result):
        if l == n and r == n:
            return self.ret.append(result)
        if l < n:
            self._gen(l + 1, r, n, result + '(')
        if r < l:
            self._gen(l, r + 1, n, result + ')')


s = Solution()
print(s.generateParenthesis(3))
            
            