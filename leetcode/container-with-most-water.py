################################################################################
# Question:
# Container With Most Water

# Given n non-negative integers a1, a2, ..., an , where each represents a 
# point at coordinate (i, ai). n vertical lines are drawn such that the two 
# endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together 
# with x-axis forms a container, such that the container contains the most 
# water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) 
# the container can contain is 49.
# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
################################################################################
# Solution Notes:

# Time Complexity O(n)

# Set left = 0 and right = len
# Get left and right closer such that the smaller one of them gets close.abs
# Calc area at each stage and store the max
# return the max
################################################################################


class Solution(object):
    
    def calc_area(self, left, right, height):
        return (right - left) * min(height[left], height[right])
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        _max = 0
        _max_index = None
        while left < right:
            area = self.calc_area(left, right, height)
            if area > _max:
                _max = area
                _max_index = (left, right)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return _max       