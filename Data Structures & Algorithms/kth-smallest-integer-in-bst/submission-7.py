# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Using a iterative soltution using a stack
    We essentially go through the tree, mainly traversing through the left subtree, going add adding each value to our stack
    then stop when null, pop our last value on the stack, and set out pointer there.
    Then increment n by one, check if its our desired value, otherwise set curr to the right subtree of that.
    This visited each node at maximum once, hence the alogrithm has a O(n) time complexity and a O(n) space complexity
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
