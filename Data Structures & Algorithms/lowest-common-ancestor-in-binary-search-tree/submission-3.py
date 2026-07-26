# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """ 
    Idea is to look for the "split", where p and q split of from the tree.
    So our steps are to have a pointer at the root called curr, 
    Then iterate until we find this split, by checking 3 things:
    if curr < (p or q), then we move curr pointer to the right
    if "" > p or q, move curr to the right
    else (we are at the split), we return curr.
    Since we only visit each of the nodes once, this has a O(n) time complexity and a O(1) Space complexity since not storing anything but the 2 pointers
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val :
                curr = curr.right
            else:
                return curr