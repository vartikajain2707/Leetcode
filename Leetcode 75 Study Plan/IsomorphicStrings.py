# Leetcode 75 Days of Study Plan 
# Day 2

def isIsomorphic(self, s: str, t: str) -> bool:
        dic={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]]=t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        dic={}
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]]=s[i]
            else:
                if dic[t[i]] != s[i]:
                    return False
        return True
                
# Example 1:

# Input: s = "egg", t = "add"
# Output: true