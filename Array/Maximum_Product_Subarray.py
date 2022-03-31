# Input:
# N = 5
# Arr[] = {6, -3, -10, 0, 2}
# Output: 180
# Explanation: Subarray with maximum product
# is [6, -3, -10] which gives product as 180


def maxProduct(self,arr, n):
    maxi=arr[0]
    mn=arr[0]
    mx=arr[0]
    for i in range(1,n):
        if arr[i]<0:
            mx,mn=mn,mx
        mx=max(arr[i],arr[i]*mx)
        mn=min(arr[i],arr[i]*mn)
        maxi=max(maxi,mx)
    return maxi