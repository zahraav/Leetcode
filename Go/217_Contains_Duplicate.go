func containsDuplicate(nums []int) bool {
    freqmap:=make(map[int]int)
    for i:=0;i<len(nums);i++{
        temp:=nums[i]
        if freqmap[temp]>0{
            return true
        }
        freqmap[temp]++
    }
    return false
}