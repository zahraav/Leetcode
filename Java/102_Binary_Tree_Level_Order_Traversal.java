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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();   
        List<List<Integer>> res= new ArrayList<>();
        q.add(root);
        while(!q.isEmpty()){
            List<Integer> l = new ArrayList<>();
            int size=q.size();
            for(int i=0;i<size;i++){
                TreeNode node=q.poll();
                if (node!=null){
                    l.add(node.val);
                    q.add(node.left);
                    q.add(node.right);                    
                }
            }
            if(l.size()>0){
                res.add(l);
            }
        }
        return res;
    }
}
