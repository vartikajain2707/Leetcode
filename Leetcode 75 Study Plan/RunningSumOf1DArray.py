# Leetcode 75 Days of Study Plan 
# Day 1
def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        sub=0
        for i in range(len(nums)):
            sub+=nums[i]
            ans.append(sub)
        return ans

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].