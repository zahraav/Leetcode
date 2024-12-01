class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> res= new HashMap();
        for(String s:strs){
            int[] count = new int[26];
            for(char ch:s.toCharArray()){
                count[ch-'a']++;
            }
            String k=Arrays.toString(count);
            res.putIfAbsent(k,new ArrayList<>());
            res.get(k).add(s);
        }
        return new ArrayList<>(res.values());
    }
}