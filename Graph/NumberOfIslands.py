# Leetcode 200
def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        def isValid(i,j,m,n,grid):
            if i>=0 and j>=0 and i<m and j<n and grid[i][j]=='1':
                
                return True
            return False
        def dfs(i,j,m,n,grid):
            grid[i][j]='0'
            if isValid(i+1,j,m,n,grid):
                dfs(i+1,j,m,n,grid)
            if isValid(i-1,j,m,n,grid):
                dfs(i-1,j,m,n,grid)
            if isValid(i,j+1,m,n,grid):
                dfs(i,j+1,m,n,grid)
            if isValid(i,j-1,m,n,grid):
                dfs(i,j-1,m,n,grid)
        ans=0
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]=='1':
                    dfs(i,j,m,n,grid)
                    ans+=1
                    
        return ans
    
#     In this we have to find number of groups of connected ones in the graph. we will use dfs approach in this. first we need to find whether the index position is valid or not. for that we have defined a function 'isValid' which is checking for the calidity of the index.
# Now in dfs function we will check if the index is valid we will call dfs function recursively. Now when the function ends we will do 'ans+=1' to calculate the number of islands. 
# In the end return ans.
#
# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1