# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    We can do a slow fast pointer method, one moves 1 at a time, other moves 2
    If these ever meet before one of them reaches end, its got a loop, else it doesnt.
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next            
            if slow == fast:
                return True

        return False