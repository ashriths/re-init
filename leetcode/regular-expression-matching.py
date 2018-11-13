################################################################################
# Question:

# 10. Regular Expression Matching - Hard


# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:

# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
################################################################################


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print "isMatch(s=", s, ",p=", p, ")"
        if len(s) == 0 and len(p) == 0:
            return True
        elif len(p) >= 2:
            pc1 = p[0]
            pc2 = p[1]
            sc = s[0] if len(s) > 0 else ""
            
            if pc2 != '*':
                if sc!= "" and (pc1 == '.' or pc1 == sc):
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
            else:
                if sc != "" and (sc == pc1 or pc1 == '.'):
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                else:
                    return self.isMatch(s, p[2:])
        elif len(p)==1 and len(s)==1:
            return s[0] == p[0] or p[0] == '.'

        return False
   