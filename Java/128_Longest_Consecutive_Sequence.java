class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> n=new HashSet<>();
        for(int i:nums){
            n.add(i);
        }
        int max=0;
        for(int i:nums){
           if(!n.contains(i-1)){
                int l=1;
                while(n.contains(i+l)){
                    l++;
                }
                max=Math.max(max,l);
           }
        }
        return max;

    }
}
