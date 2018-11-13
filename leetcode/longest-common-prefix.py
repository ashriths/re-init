################################################################################
# Question:

# 14. Longest Common Prefix - Easy


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.
################################################################################


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s_strs = sorted(strs, key=lambda x: len(x))
        if len(s_strs) < 1:
            return ''
        smallest = s_strs[0]
        for i in range(len(smallest)-1, -1, -1):
            sub_st = smallest[:i+1]
            print i, sub_st
            for j in s_strs[1:]:
                if not j.startswith(sub_st):
                    break
            else:
                return sub_st
        return ''
        