# // Given a binary array nums, return the maximum number of consecutive 1's in the array.

# // Example 1:

# // Input: nums = [1,1,0,1,1,1]
# // Output: 3
# // Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

class solution:
    def FindMaxConsecutivesOnes(nums):
        no_of_one = 0
        max_no_of_one = 0

        for i in nums:
            if i==1:
                no_of_one += 1
            else:
                if no_of_one > max_no_of_one:
                    max_no_of_one = no_of_one
                no_of_one = 0
        if no_of_one > max_no_of_one:
                    max_no_of_one = no_of_one
        return max_no_of_one
    
    print(FindMaxConsecutivesOnes([1,1,0,1,1,1]))