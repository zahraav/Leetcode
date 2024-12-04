class Solution {

    public String encode(List<String> strs) {
        StringBuilder res=new StringBuilder();
        for(String s: strs){
            res.append(s.length()).append("#").append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> res=new ArrayList<String>();
        int index=0;
        while(index<str.length()){
            String s="";
            while(index<str.length() && Character.isDigit(str.charAt(index))){
                s+=str.charAt(index);
                index++;
            }
            if (s.isEmpty()) {
                throw new IllegalArgumentException("Invalid encoded string format.");
            }
            int size=Integer.parseInt(s);
            index++;//remove #
            res.add(str.substring(index,index+size));
            index+=size;
        }
        return res;

    }
}
