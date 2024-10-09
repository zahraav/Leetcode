class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        maxd=[]

        for i in root.children:
            maxd.append(self.maxDepth(i))

        if not maxd: # no child
            return 1
       
        return 1+max(maxd)