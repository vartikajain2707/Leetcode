# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation: 
# arr[0] + arr[1] = 1 + 5 = 6 
# and arr[1] + arr[3] = 5 + 1 = 6

def getPairsCount(self, arr, n, k):
        dic=dict()
        count=0
        for i in range(n):
            if k-arr[i] in dic:
                count+=dic[k-arr[i]]
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
        return count