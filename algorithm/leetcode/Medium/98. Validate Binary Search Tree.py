#leetcode 98. Validate Binary Search Tree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    
    def __init__(self):
        self.res = []
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []
        self.inorderTraversal(root)
        last = None
        for n in self.res:
            if last is not None:
                if last >= n:
                    return False
            last = n
        return True
                        
    
    def inorderTraversal(self, root):
        """
        :rtype: List[]
        """
        if root and root.left:
            self.inorderTraversal(root.left)
        if root:
            self.res.append(root.val)
        if root and root.right:
            self.inorderTraversal(root.right)
    
    def isValidBST_2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes = []
        while root:
            nodes.append(root)
            root = root.left
        last = None
        while nodes:
            n = nodes.pop()
            if last is not None:
                if last.val >= n.val:
                    return False
            last = n
            #考查完这个元素之后，再考查它的右子树
            m = n.right
            while m:
                nodes.append(m)
                m = m.left
        return True
            
                
    def isValidBST_3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validation(root, None, None)
    
    def validation(self, node, min, max):
        """
        rtype
        如果左子树的 max 比 node 小
          且右子树的 min 比 node 大
        则成立
        """
        if not node: return True
        if min is not None and min >= node.val: return False
        if max is not None and max <= node.val: return False
        return self.validation(node.left, min, node.val) and self.validation(node.right, node.val, max)
        
        
            
            
            
        
        
t10 = TreeNode(10) #root
t20 = TreeNode(20)
t30 = TreeNode(30)
t21 = TreeNode(21)
t31 = TreeNode(31)

t10.left = t20
t10.right = t30
t30.left = t21
t30.right = t31

######
t1 = TreeNode(1)
t2 = TreeNode(2) #root
t3 = TreeNode(3)

t2.left = t1
t2.right = t3

######
t0 = TreeNode(0)
tm1 = TreeNode(-1)

t0.right = tm1

s = Solution()
#s.inorderTraversal(t2)
#print(s.res)
#print(s.isValidBST(t0))

print(s.isValidBST_3(t0))