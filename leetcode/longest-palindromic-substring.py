################################################################################
# Question:
# Longest Palindromic Substring

# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
################################################################################
# Solution Notes:
# Time Complexity: O(n^2)
################################################################################
class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 1
        max_index = (0,0)
        for i in xrange(0, n):
            #print i
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                
                if right - left + 1 > max_len:
                    #print left,right, s[left:right+1]
                    max_len = right - left + 1
                    max_index = (left, right)
                left -= 1
                right += 1
                
            left = i-1
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    #print left,right, s[left:right+1]
                    max_len = right - left + 1
                    max_index = (left, right)
                left -= 1
                right += 1
        return s[max_index[0]:max_index[1]+1]
        
        