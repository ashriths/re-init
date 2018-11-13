################################################################################
# Question:

# 3Sum

# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? Find all unique triplets in the array which 
# gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
################################################################################
# Solution Note:

# Trivial solution would be to have 3 loops with O(n^3)
# Sorting reduces the complexity to O(n^2)

# Two ways again:

# Constant space complexity:
#     1. Sort it
#     2. Fix one number using a loop. 
#     3. Get the left and right corners and move closer to center based on whether its small or bigger than the sum required.

# Additional space:
#     1. Sort it
#     2. Use hashmap to store intermediate sum
#     3. Use the sum of numbers and the stored value in hashmap to get results
################################################################################
class Solution(object):            
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print nums
        ret = set()
        for k,i in enumerate(nums):
            rem = 0 - i
            l = k+1
            r = len(nums)-1
            while l < r:
                #print i, nums[l], nums[r], rem
                if nums[l] + nums[r] == rem:
                    ret.add((i, nums[l], nums[r]))
                    l += 1
                elif nums[l] + nums[r] > rem:
                    r -= 1
                else:
                    l += 1
        return list(list(x) for x in ret)
            
        