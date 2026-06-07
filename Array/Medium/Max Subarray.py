# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

class solutions:
    def maxSubarray(nums):
        sum = 0
        maxs = float('-inf')
        for i in nums:
            sum += i
            maxs = max(maxs, sum)
            if sum < 0:
                sum = 0
        return maxs
