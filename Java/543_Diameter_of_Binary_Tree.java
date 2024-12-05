/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        if(root==null){
            return 0;
        }
        int leftHight=maxHight(root.left);
        int rightHight=maxHight(root.right);
        int diameter=leftHight+rightHight;

        int t=Math.max(diameterOfBinaryTree(root.left),diameterOfBinaryTree(root.right));

        return Math.max(t,diameter);
        
    }
    private int maxHight(TreeNode node){
        if(node==null){return 0;}
        return Math.max(maxHight(node.left),maxHight(node.right))+1;
    }
}
