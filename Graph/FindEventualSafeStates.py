# Leetcode 802
def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def cyclic(graph, visited, dfsVidited,s,presentLoop):
            visited[s]=True
            dfsVisited[s]=True
            data =graph[s]
            for i in data:
                if visited[i]==False:
                    if cyclic(graph,visited,dfsVisited,i,presentLoop):
                        presentLoop[s]=True
                        return presentLoop
                elif visited[i]==True and dfsVisited[i]==True:
                    presentLoop[s]=True
                    return presentLoop        
            dfsVisited[s]=False
            return False
        
        n=len(graph)
        visited=[False]*n
        dfsVisited=[False]*n
        presentLoop=[False]*n
        for i in range(n):
            if visited[i]==False:
                cyclic(graph,visited,dfsVisited,i,presentLoop)
        ans=[]
        print(presentLoop)
        for i in range(n):
            if presentLoop[i]==False:
                ans.append(i)
        return ans
    
#    To solve this graph ques, you need one prerequisite of detect cycle in directed graph. This is a variation of ques detect cycle in directed graph.
# Similar to that we will find if the cycle is present in it or not. If cycle is present then we will not include that node. And to keep record of nodes that which node is involved in cycle we will take an array 'presentLoop' and if the current node is involved in loop we will insert True in that node's position in the presentLoop array.
# And in the end return the values which are False in presentLoop array.
# Example 1 
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
