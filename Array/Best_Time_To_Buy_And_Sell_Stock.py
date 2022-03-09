# leetcode Easy
# 1. We will traverse the array while storing the minimum in mini.
# 2. if prices[i]<mini:
#         mini=prices[i]
#    else:
#         maxi=max(maxi,prices[i]-mini)
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

 
def maxProfit(self, prices) -> int:
        n=len(prices)
        maxi=0
        mini=1000000000
        for i in range(n):
            if prices[i]<mini:
                mini=prices[i]
            else:
                maxi=max(maxi,prices[i]-mini)
        return maxi