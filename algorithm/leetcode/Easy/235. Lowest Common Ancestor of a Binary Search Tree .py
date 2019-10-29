#leetcode 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        
        从根节点出发，开始层先遍历，考查每一个节点
        如果该节点 left < min 则向右子树查找
        如果该节点 right > max 则向左子树查找
        否则，该节点为 LCR
        """
        nodes = [root]
        mi = min(p.val, q.val)
        ma = max(p.val, q.val)
        while nodes:
            n = nodes.pop(0)
            if n.val < mi:
                nodes.append(n.right)
            elif n.val > ma:
                nodes.append(n.left)
            else:
                return n
        return None

t6 = TreeNode(6) #root
t2 = TreeNode(2)
t8 = TreeNode(8)

t6.left = t2
t6.left = t8

s = Solution()
print(s.lowestCommonAncestor(t6, t6, t8).val)