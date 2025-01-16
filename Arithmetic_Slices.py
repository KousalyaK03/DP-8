# Approach:
# An arithmetic slice is a subarray of at least 3 elements where the difference between consecutive elements is the same.
# To count the number of arithmetic slices in the given array, we can iterate through the array and track the length of the current arithmetic subarray.
# If a subarray is arithmetic, we increment a counter that tracks the number of valid subarrays.
# For each valid arithmetic subarray, the number of subarrays formed by it will be equal to the length of the subarray minus 2.
# Time Complexity: O(n), where n is the length of the array nums. We only need to iterate through the array once.
# Space Complexity: O(1), since we use constant extra space.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Edge case: if the array has less than 3 elements, return 0 as no arithmetic subarrays are possible
        if len(nums) < 3:
            return 0
        
        # Variable to store the total count of arithmetic slices
        count = 0
        # Variable to track the length of the current arithmetic slice
        current_length = 0
        
        # Start iterating from the second element (index 1)
        for i in range(2, len(nums)):
            # If the current element maintains the arithmetic sequence with the previous two elements
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                # If it's part of an arithmetic sequence, increment the current length
                current_length += 1
                # Add the number of subarrays formed by this slice (current_length subarrays)
                count += current_length
            else:
                # Reset current_length if the arithmetic sequence breaks
                current_length = 0
        
        return count
