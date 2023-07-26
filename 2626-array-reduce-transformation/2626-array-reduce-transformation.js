/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    if (nums.length===0){
    return init
    }
    let ans=0
    for(let i=0;i<nums.length;i++){
        if (i===0){
            ans=fn(init,nums[i])
        }
        else{
            ans=fn(ans,nums[i])
        }
    }
    return ans
    
};