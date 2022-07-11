# Leetcode 75 Days of Study Plan 
# Day 1
def pivotIndex(self, nums: List[int]) -> int:
        i=0
        l=sum(nums[:0])
        r=sum(nums[1:])
        
        while i<len(nums)-1:
            if l==r:
                return i
            l+=nums[i]
            r-=nums[i+1]
            i+=1
        if sum(nums[:len(nums)-1])==0:
            return len(nums)-1
        return -1

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11