################################################################################
# Question:

# 128. Longest Consecutive Sequence - Hard


# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

################################################################################

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        al = set(nums)
        m = 0
        for num in nums:
            if num - 1 not in al:
                s = 0
                i = 0
                while num +i in al:
                    s += 1
                    i = i + 1
                m = max(m, s)
        return m