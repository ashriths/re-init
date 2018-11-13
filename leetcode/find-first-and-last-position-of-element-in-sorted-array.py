################################################################################
# Question:

# 34. Find First and Last Position of Element in Sorted Array - Medium

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
################################################################################

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        return self.findRange(nums, target, 0, len(nums)-1)
        
    def findRange(self, nums, target, left, right):
        mid = left + ((right - left + 1)/2)
        #print left, mid, right
        leftRange = [-1,-1]
        rightRange = [-1,-1]
        if mid > left:
            leftRange = self.findRange(nums, target, left, mid - 1)
        if mid < right:
            rightRange = self.findRange(nums, target, mid+1, right)
        
        if nums[mid] == target:
            ran = (mid if leftRange[0] == -1 else leftRange[0], mid if rightRange[1] == -1 else rightRange[1])
            return ran
        else:
            if leftRange == [-1,-1]:
                return rightRange
            return leftRange
            