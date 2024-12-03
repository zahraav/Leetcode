class Solution {
    public int findNonMinOrMax(int[] nums) {
        if (nums == null || nums.length < 3) {
            return -1;
        }
        PriorityQueue<Integer> minHeap=new PriorityQueue<>();
        for(int i:nums){
            minHeap.offer(i);
            if(minHeap.size()>3){
                break;
            }
        }

        minHeap.poll();
        return minHeap.peek();
    }
}