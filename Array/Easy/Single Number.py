# // Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# // You must implement a solution with a linear runtime complexity and use only constant extra space.

# // Example 1:

# // Input: nums = [2,2,1]
# // Output: 1

class solution:
    def singleNumber(nums):
        res = 0
        for i in nums:
            res ^= i
        return res
    print(singleNumber([1,2,1,2,3,4,4]))