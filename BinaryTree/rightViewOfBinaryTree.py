def rightView(self,root):
        
    # code here
    ans=[]
    queue=[]
    queue.append(root)
    if root is None:
        return ans
    while len(queue)>0:
        sol=[]
        for i in range(len(queue)):
            curr=queue.pop(0)
            sol.append(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        ans.append(sol[-1])
    return ans