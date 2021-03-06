# leetcode 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.maxDepth = 1
        self._dfs(root, 1)
        return self.maxDepth
        
    def _dfs(self, node, level):
        if not node: return
        if level > self.maxDepth:
            self.maxDepth = level
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
    
    def _bfs(self, root):
        if not root:
            return 0
        ret = 0
        q = [root]
        levelQ = []
        while q:
            ret += 1
            while q:
                n = q.pop(0)
                if n:
                    levelQ.append(n)
            while levelQ:
                n = levelQ.pop(0)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return ret