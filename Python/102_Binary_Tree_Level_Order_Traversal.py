# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res={}
        def helper(node,depth):
            if node is None:
                return
            if depth not in res:
                res[depth]=[node.val]
            else:
                res[depth].append(node.val)
            if node.left: 
                helper(node.left,depth+1)
            if node.right: 
                helper(node.right,depth+1)
        helper(root,0)
        return [res[depth] for depth in res]

