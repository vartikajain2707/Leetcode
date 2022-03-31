def bottomView(self, root):
    def vertical(root,d,l,m):
        # Vertical traversal of tree.
        if root is None:
            return 
        if d not in m:
            m[d]=[root.data,l]
        elif m[d][1]<=l:
            m[d]=[root.data,l]
        vertical(root.left,d-1,l+1,m)
        vertical(root.right,d+1,l+1,m)
    m={}
    ans=[]
    vertical(root,0,0,m)
    for i in sorted(m.keys()):
        ans.append(m[i][0])
    return ans