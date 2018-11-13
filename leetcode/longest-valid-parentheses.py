################################################################################
# Question:
# 32. Longest Valid Parentheses - Hard

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

################################################################################


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        _max = 0
        cur = 0
        l = []
        for i,c in enumerate(s):
            
            if len(stack) == 0 and c == ')':
                l.append(0)
            elif c == '(':
                stack.append(i)
                l.append(0)
            else:
                j = stack.pop()
                l[j] = 1
                l.append(1)
            #print i,c, l
        for i in l:
            if i == 0:
                cur = 0
            else:
                cur += 1
            _max = max(cur, _max)
        return _max
 