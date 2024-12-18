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
    public boolean isBalanced(TreeNode root) {
        if( root ==null){
            return true;
        }  
        if(Math.abs(maxHight(root.left)-maxHight(root.right))>1){
            return false;
        }
        return isBalanced(root.left) && isBalanced(root.right);
    }
    private int maxHight(TreeNode node){
        if(node==null){return 0;}
        return Math.max(maxHight(node.left),maxHight(node.right))+1;
    }
}
