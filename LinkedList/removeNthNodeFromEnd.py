# This Question is available on interview bit with the name remove Nth node from the end of list
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
	def removeNthFromEnd(self, A, B):
            if(A is None):
                return None
            prev=None
            curr=A
            forward=A
            for i in range(0,B):
                forward=forward.next
                if(forward is None):
                    return A.next
                
            while(forward is not None):
                forward=forward.next
                prev=curr
                curr=curr.next

            prev.next=curr.next
            return A 