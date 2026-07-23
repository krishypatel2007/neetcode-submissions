# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    """
    Idea is to implement merge 2 lists method from before, doing lists one by one
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i], lists[i-1])
        return lists[-1]

    def mergeList(self, l1, l2): # see idea for this from other problem
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            

        tail.next = l1 or l2
        return dummy.next