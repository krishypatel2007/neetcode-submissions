# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    """
    Idea is to check when root and subroot are equal, then implement the SameTree Method to check if trees are same.
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.SameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def SameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.SameTree(p.right, q.right) and self.SameTree(p.left, q.left)
        else:
            return False