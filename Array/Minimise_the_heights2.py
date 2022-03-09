# GFG Medium
# first we will sort the array
# If we increase the smallest tower by k and decrease the longest tower by k, the difference between the two towers will be minimum.
# So this is we are doing with every tower and comparing.


# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output: 5
# Explanation:
# The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5



def getMinDiff(self, arr, n, k):
        # sorting the array
        arr.sort()
        # storing the difference of smallest and largest tower in diff
        diff=arr[n-1]-arr[0]
        mini=1000000000
        maxi=-1000000000
        for i in range(1,n):
            # if the height of the current tower is less than k we will continue
            if arr[i]-k<0:
                continue
            # we are comapring each tower
            # 1. trying to compare each tower by adding k to it and then comparing it with the height of last tower after decreasing it by k.
            # if we find that by adding k to any tower its height becomes greater than arr[n-1]-k then the height of that tower will be maximum.
            # 2.and similarly we are doing with the smallest tower.
            # comparing arr[0]+k and the height of each tower after subtracting it with k, if any arr[i]-k is less than arr[0]+k then we will update our mini.
            maxi=max(arr[n-1]-k,arr[i-1]+k)
            mini=min(arr[0]+k,arr[i]-k)
            diff=min(maxi-mini,diff)
        return diff