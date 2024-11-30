class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> res=new HashSet<Integer>();
        for(int n : nums){
            if(res.contains(n)){
                return true;
            }
            res.add(n);
        }
        return false;
    }        
}