# Given an array of integers nums, return the value of the largest element in the array

# Example 1

# Input: nums = [3, 3, 6, 1]
# Output: 6
# Explanation: The largest element in array is 6

# Example 2

# Input: nums = [3, 3, 0, 99, -40]
# Output: 99
# Explanation: The largest element in array is 99

class solution:
    def largestElements(nums):
        max = 0
        for i in nums:
            if i > max:
                max = i
        
        return max
    
    print (largestElements([3, 3, 0, 99, -40]))
    