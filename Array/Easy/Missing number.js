// Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1

// Example 1

// Input: nums = [2, 3, 4, 5, 3], target = 3
// Output: 1
// Explanation:
// The first occurence of 3 in nums is at index 1
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let n = nums.length
    let tsum = (n*(n+1))/2
    console.log(tsum)
    let asum = 0
    for(let i=0; i<n; i++){
        asum += nums[i]
    }
    return tsum - asum

};