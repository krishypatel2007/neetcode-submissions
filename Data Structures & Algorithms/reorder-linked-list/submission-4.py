# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Idea is to:
    -> Use slow fast pointer method to find midpoint and split lists into l1,l2 
    -> Reverse l2
    -> Merge the reversed l2 onto l1 in the correct order for submission
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Split lists
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse 2nd list
        second = slow.next # curent pointer
        prev = slow.next = None # previouse pointer
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge our two lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
    


        