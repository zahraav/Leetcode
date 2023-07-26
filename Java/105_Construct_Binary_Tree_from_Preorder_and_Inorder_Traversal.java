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

    public TreeNode buildTree(int[] preorder, int[] inorder) {

        if (preorder.length==0 || inorder.length==0){
            return null; 
        }
        Map<Integer,Integer> inmap=new HashMap<>();
        for( int i =0 ; i< inorder.length;i++){
            inmap.put(inorder[i],i);
        }
        return helper(preorder,inorder,inmap,0,preorder.length-1,0,inorder.length-1);
    }
    public TreeNode helper(int[] preorder, int[] inorder, Map<Integer,Integer> inmap, int prestart, int preend,int instart,int inend){
        if (prestart>preend || instart>inend){
            return null;
        }
        TreeNode root=new TreeNode(preorder[prestart]);
        int rootindex=inmap.get(root.val);
        int leftside=rootindex-instart;

        root.left=helper(preorder,inorder,inmap,prestart+1,prestart+leftside, instart,rootindex-1);
        root.right=helper(preorder,inorder,inmap, prestart+leftside+1, preend,rootindex+1,inend);
        return root;

    }
}
