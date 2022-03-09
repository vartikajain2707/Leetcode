#GFG Medium
#  Kadane's algorithm is used to find the largest sum contiguous subarray.
# If the sum of any subarray is less than 0 then we will male the curr_sum=0
# because if the sum(subarray)<0, it is only decreasing the total sum. Hence we will not include it.
# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.


def maxSubArraySum(self,arr,N):
        ##Your code here
        maxSum=-1000000000
        currSum=0
        for i in arr:
            currSum+=i
            maxSum=max(currSum,maxSum)
            if currSum<0:
                currSum=0
        return maxSum