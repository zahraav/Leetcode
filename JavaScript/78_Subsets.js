/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    const result=[];
    
    function dfs(i,cursubset){
        if (i== nums.length){
            result.push([...cursubset]);
            return
        }
        cursubset.push(nums[i]);
        dfs(i+1,cursubset);

        cursubset.pop();
        dfs(i+1,cursubset);
    }
    dfs(0,[]);
    return result;
};


