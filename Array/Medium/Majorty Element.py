# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

#   | O(n)  | Boyrre Moore Votin algorithim

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        strength = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                strength += 1
            else:
                if strength == 0:
                    candidate = nums[i]
                    strength += 1
                else:
                    strength -= 1
        return candidate