# Input:
# N = 6
# arr[] = {3,0,0,2,0,4}
# Output:
# 10
# total trapped water: 3+3+1+3=10

def trappingWater(self, arr,n):
    left=[0]*n
    right=[0]*n
    water=0
    left[0]=arr[0]
    for i in range(1,n):
        left[i]=max(arr[i],left[i-1])
    right[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        right[i]=max(arr[i],right[i+1])
    for i in range(n):
        water+=min(left[i],right[i])-arr[i]
    return water