# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Idea is to have a recursive function where we check the root, if not same, return false, and if both empty, return True
    If same, we check left and right subtree using the same method. 
    If checks are all good, we return True ie tree are the same
    This will have O(n) time complexity and O(n) space complexity, n = no of nodes in tree.
    This is because we check each node at most once, and compare each of the subtree's node.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and  not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False