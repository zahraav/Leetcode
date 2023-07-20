# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self,node,left,right)->bool:
        if node is None:
            return True
        if not (left<node.val and node.val< right):
            return False
        return self.isValid(node.left,left,node.val)and self.isValid(node.right,node.val,right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root,float("-inf"),float("inf"))