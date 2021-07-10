# This Question is available on interview bit with the name sort the binary linked list
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        temp=A
        zeroes=0
        ones=0
        while(temp is not None):
            if(temp.val==0):
                zeroes+=1
            else:
                ones+=1
            temp=temp.next
        temp=A
        while(zeroes>0):
            temp.val=0
            temp=temp.next
            zeroes-=1
        while(ones>0):
            temp.val=1
            temp=temp.next
            ones-=1
        return A
