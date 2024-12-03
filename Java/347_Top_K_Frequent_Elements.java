class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> freq= new HashMap();
        for(int i:nums){
            freq.put(i,freq.getOrDefault(i,0)+1);
        }
        
        PriorityQueue <Map.Entry<Integer,Integer>> minHeap=new PriorityQueue <>((a,b) -> a.getValue()-b.getValue());
        //add to minheap:
        for(Map.Entry<Integer,Integer> en: freq.entrySet()){
            minHeap.offer(en);
            if(minHeap.size()>k){
                minHeap.poll(); // remove the one with min freq
            }
        }

        int[] res= new int[k];
        int index=k-1;
        while(!minHeap.isEmpty()){
            res[index]=minHeap.poll().getKey();
            index--;
        }

        return res;
    }
}