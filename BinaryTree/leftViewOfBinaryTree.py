'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    
    # code here
    queue=deque([])
    solution=[]
    queue.append(root)
    if root is None:
        return solution
    while len(queue)>0:
        ans=deque([])
        length=len(queue)
        for i in range(length):
            curr=queue.popleft()
            ans.append(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        sol=ans.popleft()
        solution.append(sol)
    return solution