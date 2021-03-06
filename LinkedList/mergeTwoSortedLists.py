# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(-1)
        current=dummy
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while(l1 is not None and l2 is not None):
            if(l1.val<l2.val):
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
            current.next=l1 or l2
        return dummy.next