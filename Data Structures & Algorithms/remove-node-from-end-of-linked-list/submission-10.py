# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Idea is to have 2 pointers, left, right from dummy node 0 -> head so that:
    - right node finds node by taking n steps to remove at (n index)
    - say list length is L
    - now move left and right node right at a time until right is null 
     ie left now at 0 + (L - n + 1) = L - (n-1) ie the node BEFORE the one u want to remove
    - skip the nth node using left then return dummy.next
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head

        # right pointer at the nth node
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # adjust left pointer to n-1 node
        while right:
            left = left.next
            right = right.next
        
        # remove the nth node
        left.next = left.next.next
        return dummy.next