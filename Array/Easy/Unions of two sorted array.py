# // Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.

# // The union of two arrays is an array where all values are distinct and are present in either the first array, the second array, or both.

# // Example 1

# // Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
# // Output: [1, 2, 3, 4, 5, 7]
# // Explanation:
# // The elements 1, 2 are common to both, 3, 4, 5 are from nums1 and 7 is from nums2

class solutions:
    def unions(nums1, nums2):
        n = len(nums1)
        m = len(nums2)
        temp = []
        i, j = 0, 0
        while(i < n and j < m):
            if nums1[i] < nums2[j]:
                if len(temp) == 0 or temp[-1] != nums1[i]:
                    temp.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                if len(temp) == 0 or temp[-1] != nums1[i]:
                    temp.append(nums1[i])
                i += 1
                j += 1
            else:
                if len(temp) == 0 or temp[-1] != nums2[j]:
                    temp.append(nums2[j])
                j += 1
        
        if i < n:
            while i < n:
                temp.append(nums1[i])
                i += 1
        if j < m:
            while j < m:
                temp.append(nums2[j])
                j += 1
        
        return temp
    
    print(unions([1, 2, 3, 4, 5],[1, 2, 7]))