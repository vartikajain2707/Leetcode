# Leetcode 733
def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        fill=image[sr][sc]
        def isValid(i,j,m,n,image):
            if i>=0 and i<m and j>=0  and j<n and image[i][j]==fill:
                return True
            return False
        def dfs(sr,sc,m,n,image):
            image[sr][sc]=color
            if isValid(sr+1,sc,m,n,image):
                dfs(sr+1,sc,m,n,image)
            if isValid(sr-1,sc,m,n,image):
                dfs(sr-1,sc,m,n,image)
            if isValid(sr,sc+1,m,n,image):
                dfs(sr,sc+1,m,n,image)
            if isValid(sr,sc-1,m,n,image):
                dfs(sr,sc-1,m,n,image)
        if fill==color:
            return image
        dfs(sr,sc,m,n,image)
        return image
            
#     The approach for this question is similar to the ques NumeberOfIslands. If the color of image[sr][sc]==color we will simply return the image.
# The approach will be dfs function + isValid function. Dfs function will be called recursilvely for all the adjacent nodes and isValid function is used to check if the node is valid or not (it should not be out of bound).

# Example 1:


# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.