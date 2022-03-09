#GFG Medium
#  We will be using heap to find the Kth smallest element.
# max heap will be used.
# we will push elements in the heap, we know it is a max heap so it will push the elements in the decreasing(descending) manner from top to bottom.
# max heap will keep the max element at the top of the heap.
# if len(heap)>k then we will pop the top.
# Now after the loop ends, we will have the kth smallest element at the top of the heap.
# Therefore we will return the top the heap.


# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7

from heapq import heappop, heappush, heapify
class Solution:
    def kthSmallest(self,arr, l, r, k):
        heap=[]
        heapify(heap)
        for i in arr:
            heappush(heap,-1*i)
            if len(heap)>k:
                heappop(heap)
        return heap[0]*-1