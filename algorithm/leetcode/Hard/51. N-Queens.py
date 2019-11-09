# leetcode 51. N-Queens


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.ret, self.col, self.pie, self.na = [], [], [], []
        self._gen(0, [])
        return self._genBoards(n, self.ret)
        
    
    def _gen(self, row, result):
        if row >= self.n:
            return self.ret.append(result)
        for col in range(self.n):
            if col in self.col or col + row in self.pie or row - col in self.na:
                continue
            
            self.col.append(col)
            self.pie.append(col + row)
            self.na.append(row - col)
            
            self._gen(row + 1, result + [col])
            
            self.col.remove(col)
            self.pie.remove(col + row)
            self.na.remove(row - col)
    
    def _genBoards(self, n, result):
        ret = []
        for board in result:
            b = []
            for i in board:
                b.append("."*i + "Q" + "."*(n - i - 1))
            ret.append(b)
        return ret


s = Solution()
print(s.solveNQueens(5))
                        