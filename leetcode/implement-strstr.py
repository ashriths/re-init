################################################################################
# Question:

# 28. Implement strStr() - Easy

# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

################################################################################


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        p = self.preProcess(needle)
        #print p
        if not needle:
            return 0
        k = 0
        i = 0
        while i < len(haystack):
            #print "S[", i, "] =>", haystack[i] , "P[", k, "] =>", needle[k] 
            if haystack[i] == needle[k]:
                k += 1
                i += 1
            
            if k == len(needle):
                return i - k
            elif i < len(haystack) and haystack[i] != needle[k]:
                if k == 0:
                    i += 1
                else:
                    k = p[k-1]
        return -1
    
    def preProcess(self, needle):
        n = len(needle)
        s = [0] * len(needle)
        c = 0
        i = 1
        while i < n:
            if needle[i] == needle[c]:
                c += 1
                s[i] = c
                i += 1
            else:
                if c == 0:
                    s[i] = 0
                    i += 1
                else:
                    c = s[c-1]
        return s