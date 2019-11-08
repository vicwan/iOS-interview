#leetcode 102. Binary Tree Level Order Traversal


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret, q = [], [root]
        levelQ = []
        while q:
            while q:
                node = q.pop(0)
                if node:
                    levelQ.append(node)
            tmp = []
            while levelQ:
                n = levelQ.pop(0)
                tmp.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if tmp:
                ret.append(tmp)
        return ret
    
    def levelOrder(self, root):
        self.ret = []
        self.dfs(0, root)
        return self.ret
    def dfs(self, level, node):
        if not node: return
        if level > len(self.ret) - 1:
            self.ret.append([])
        self.ret[level].append(node.val)
        self.dfs(level + 1, node.left)
        self.dfs(level + 1, node.right)
            

                
            
            
            