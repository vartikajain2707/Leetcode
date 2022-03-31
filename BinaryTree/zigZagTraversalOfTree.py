from collections import deque
def zigZagTraversal(self, root):
    flag=False
    ans=deque([])
    queue=deque([])
    queue.append(root)
    while len(queue)>0:
        sol=deque([])
        for i in range(len(queue)):
            curr=queue.popleft()
            if flag:
                sol.appendleft(curr.data)
            else:
                sol.append(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        ans+=sol
        flag=not flag
        
    return ans