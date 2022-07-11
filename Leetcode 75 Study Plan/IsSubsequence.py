# Leetcode 75 Days of Study Plan 
# Day 2
def isSubsequence(self, s: str, t: str) -> bool:
    i=0
    j=0
    count=0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            i+=1
            j+=1
            count+=1
        else:
            j+=1
    if count==len(s):
        return True
    return False

# Input: s = "abc", t = "ahbgdc"
# Output: true