# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node:Optional[TreeNode] ,elemlist:List[int]):
        if node is None:
            return
        self.inorder(node.left,elemlist)
        elemlist.append(node.val)
        self.inorder(node.right,elemlist)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elemlist=[]
        self.inorder(root,elemlist)
        return elemlist[k-1]