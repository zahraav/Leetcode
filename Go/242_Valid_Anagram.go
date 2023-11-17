func isAnagram(s string, t string) bool {
    if len(s)!=len(t){
        return false
    }
    letterMap:=make(map[string]int)
    for i:=0;i<len(s);i++{
        fmt.Println(string(s[i]))
        letterMap[string(s[i])]++
    }
    for j:=0; j<len(t);j++{
        ch:=string(t[j])
        if val,exist :=letterMap[ch]; exist{
            if val>0{
                letterMap[ch]--    
            }else{
                return false
            }
        }
    }
    for i:=0; i<len(s);i++{
        if val,exist:=letterMap[string(s[i])];exist{
            if val>0{
                return false
            }
        }
    }
    return true
}