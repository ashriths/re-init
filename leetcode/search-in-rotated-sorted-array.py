################################################################################
# Question:

# 33. Search in Rotated Sorted Array - Medium

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
################################################################################



class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        return self.binSearch(nums, target, 0, len(nums)-1)
    
    
    def binSearch(self, nums, target, left, right):
        
        mid = left + ((right - left + 1) / 2)
        #print left, mid, right
        #print nums[left:right+1]
        #print nums[mid]
        if nums[mid] == target:
            return mid
        if (right - left + 1) <= 1:
            return -1
        if nums[left] < nums[mid]:
            if target >= nums[left] and target < nums[mid] and mid > left:
                # left part is sorted and target is in between
                #print "left"
                return self.binSearch(nums, target, left, mid-1)
            elif mid < right:
                #print "right"
                return self.binSearch(nums, target, mid+1, right)
        else:
            if target > nums[mid] and target <= nums[right] and mid < right:
                # left part is sorted and target is in between
                #print "right"
                return self.binSearch(nums, target, mid+1, right)
            elif mid > left:
                #print "left"
                return self.binSearch(nums, target, left, mid-1)
        return -1
        