################################################################################
# Question:
# Longest Substring Without Repeating Characters

# Given a string, find the length of the longest substring without repeating 
# characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer 
# must be a substring, "pwke" is a subsequence and not a substring.
################################################################################
# Solution Notes:

# Time Complexity: O(n)
# Space Complexity: O(n)

# 1. Traverse through the string by adding each char into hasmap if it has not appeared before
# 2. If it has appeared before, update the low to max(low, last occurence of char at i)
################################################################################

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        low = 0
        high = 0
        max_len = 0
        max_index = (0,0)
        for i in range(len(s)):
            if s[i] in h:
                low = max(h[s[i]] + 1, low)
                #print i, "Low -> ", low
            h[s[i]] = i
            high = i
            if high - low + 1 > max_len:
                max_len = high - low + 1
                max_index = (low, high)
        #print max_index, s[max_index[0]:max_index[1]+1]
        return max_len
            
                
        