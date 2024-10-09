# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if not node:
                return 0 
            
            if node.val>=maxval:
                count=1
                maxval=node.val
            else:
                count=0

            count+=dfs(node.left,maxval)
            count+=dfs(node.right,maxval)

            return count

        return dfs(root, float('-inf'))