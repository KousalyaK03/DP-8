# Approach:
# The problem can be solved using dynamic programming (DP). 
# Starting from the second-last row of the triangle, we compute the minimum path sum for each element 
# by adding the value of the current element to the minimum of the two adjacent elements in the row below.
# This process continues until we reach the top of the triangle. The top element will then contain the minimum path sum.
# To optimize the space, we can modify the triangle array itself, using only O(n) extra space by working with a single row.
# Time Complexity: O(n), where n is the total number of elements in the triangle. We iterate over the triangle once.
# Space Complexity: O(n), where n is the number of rows. We use O(n) space for storing the DP results (modified triangle).
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-last row and move upwards to the top
        # We modify the triangle itself to save space, reducing the space complexity to O(n)
        
        # Iterate through the rows of the triangle in reverse order
        for row in range(len(triangle) - 2, -1, -1):
            # For each element in the row, update it with the minimum path sum
            for col in range(len(triangle[row])):
                # Update the current element by adding the minimum of the two adjacent elements in the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        # The top element now contains the minimum path sum
        return triangle[0][0]
