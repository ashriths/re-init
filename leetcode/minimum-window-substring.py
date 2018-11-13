################################################################################
# Question:

# 76. Minimum Window Substring - Hard


# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

################################################################################

from collections import defaultdict, Counter
class Solution(object):
    
    def isValid(self, c1, c2):
        for c in c2:
            if c1[c] < c2[c]:
                return False
        return True
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 0:
            return ""

        seen = Counter()

        valid = False
        toSee = Counter(t)
        left = 0
        _min = len(s)
        _minIndex = (0, len(s))
        valid = False
        for i,c in enumerate(s):
            #print "Right", c, i, left, _min
            if c in toSee:
                seen[c] += 1
            if not valid:
                valid = self.isValid(seen, toSee)
            if valid:
                while s[left] not in toSee or seen[s[left]] > toSee[s[left]]:
                    if s[left] in toSee:
                        seen[s[left]] -= 1
                    left += 1
                    #print "Left =>", left
            if valid and i - left + 1 < _min:
                #print "Update min", _min, i - left + 1
                _min = i - left + 1
                _minIndex = (left, i)
        if not valid:
            return ""
        return s[_minIndex[0]:_minIndex[1]+1]
