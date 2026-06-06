# // Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.

# // Example 1

# // Input: nums = [8, 8, 7, 6, 5]
# // Output: 7
# // Explanation:
# // The largest value in nums is 8, the second largest is 7

class solutions:
    def secondLargest(nums):
        max = 0
        smax = 0
        for i in nums:
            if i > max:
                max = i
        for i in nums:
            if i < max and i > smax:
                smax = i
        return smax
    
    print(secondLargest([8, 8, 7, 6, 5]))