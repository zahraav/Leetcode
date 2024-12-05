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
    public int goodNodes(TreeNode root) {
        Queue<Pair<TreeNode,Integer>> q=new LinkedList<>();
        int res=0;
        q.add(new Pair<TreeNode,Integer>(root,root.val));
        while(!q.isEmpty()){
            int size=q.size();
            for(int i=0;i<size;i++){
                Pair<TreeNode,Integer> t=q.poll();
                TreeNode node=t.getKey();
                int v=t.getValue();
                if(node!=null){
                    res+= node.val>=v?1:0;
                    int maxv=Math.max(node.val,v);
                    q.add(new Pair<TreeNode,Integer>(node.left,maxv));
                    q.add(new Pair<TreeNode,Integer>(node.right,maxv));
                }    
            }
        }
        return res;    
    }
}
/*  public int goodNodes(TreeNode root) {
        return dfs(root,root.val);
    }
    private int dfs(TreeNode node,int maxValue){
        if(node==null){return 0;}
        int res=node.val>=maxValue?1:0;
        maxValue=Math.max(node.val,maxValue);

        res+=dfs(node.left,maxValue);
        res+=dfs(node.right,maxValue);
        return res;
    }
}*/
