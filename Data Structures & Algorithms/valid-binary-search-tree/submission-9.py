# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Idea is to do some dfs helper function to check, then return true if not node (hence passed all checks) or return false if violates conditions
    Ideally should have time complexity O(n), space complecity O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return isValid(node.left, left, node.val) and isValid(node.right, node.val, right)

        return isValid(root, float("-inf"), float("inf"))
            
        