################################################################################
# Question:

# 300. Longest Increasing Subsequence
# Medium
# 1745
# 36


# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

################################################################################

class Solution(object):
    
    def insert(self, num, s , left, right):
        if len(s) == 0:
            return 0
        if (right - left) == 0:
            return left + 1 if num > s[left] else left
        mid = int((right + left)/2)
        #print left, right, mid
        if s[mid] == num:
            return mid
        elif num < s[mid]:
            return self.insert(num, s, left, mid)
        else:
            return self.insert(num, s, mid+1, right)
    
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = []
        #print self.insert(5, s, 0, max(len(s)-1, 0))
        maxLen = 0
        for num in nums:
            index = self.insert(num, s, 0, max(len(s)-1, 0))
            if index > len(s) - 1:
                s.insert(index, num)
            else:
                s[index] = num
            #print s, num, index
            
            maxLen = max(maxLen, len(s))
        return maxLen
