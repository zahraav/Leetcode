class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap= new PriorityQueue<>((a,b)-> a-b);
        for( int i:nums){
            minHeap.offer(i);
            if(minHeap.size()>k){
                minHeap.poll();
            }
        }
        return minHeap.peek();
    }
}
//Time:
//Adding an element to the heap: O(log k)
//Iterating over nums: O(n)
//O(nlogk)

//Space:
//Heap with k space
//O(k)