class Solution {
    public int thirdMax(int[] nums) {
        PriorityQueue<Integer> minHeap=new PriorityQueue<>((a,b)->a-b);
        HashSet<Integer> seen=new HashSet<>();
        for(int i:nums){
            if(!seen.contains(i)){
                minHeap.offer(i);
                seen.add(i);
                if(minHeap.size()>3){
                    minHeap.poll();
                }
                
            }            
        }
        
        if(minHeap.size()<3){
            int maxv=Integer.MIN_VALUE;
            for(int i: minHeap){
                maxv=Math.max(i,maxv);
            }
            return maxv;
        }else{
            if(minHeap.contains(Integer.MIN_VALUE)){
                return Integer.MIN_VALUE;
            }
            return minHeap.peek();
        }
    }
}