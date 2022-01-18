# This Question is available on leetcode with the name Linked List Cycle II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        cyclefound=False
        while(fast is not None and fast.next is not None):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                cyclefound=True
                break
        if(cyclefound):
            slow=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow
        return None