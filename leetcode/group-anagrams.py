################################################################################
# Question:
# Group Anagrams

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.
################################################################################
# Solution Notes:

# 1. O(m * nlogn) solution:
# Sort each string and add it in a hashmap

# 2. O(m * n) solution:
# Assign a prime number to each alphabet and multiply to create a has of each 
# string. 
################################################################################

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for _str in strs:
            s = ''.join(sorted(_str))
            if s in d:
                d[s].append(_str)
            else:
                d[s] = [_str]
        return d.values()
        