func groupAnagrams(strs []string) [][]string {
    result:=make(map[string][]string)
    for i:=0; i< len(strs); i++{
        sorted:=sortString(strs[i])
        if _ , exist:= result[sorted]; exist{
            result[sorted]=append(result[sorted],strs[i])
        }else{
            result[sorted] = []string{strs[i]}
        }
    }
    return getvalues(result)
    
}
func getvalues(m map[string][]string)[][]string{
    res:=[][]string{}
    for _ ,s := range m{
        res=append(res,s)
    }
    return res
}
func sortString(str string)string{
    splited:=strings.Split(str,"")
    sort.Strings(splited)
    return strings.Join(splited,"")
}