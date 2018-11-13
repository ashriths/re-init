################################################################################
# Question:

# 20. Valid Parentheses - Easy


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

################################################################################

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _stack = []
        match = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for c in s:
            
            if c in ['(', '{', '[']:
                _stack.append(c)
            else:
                if len(_stack) > 0 and match[_stack[-1]] == c:
                    _stack.pop()
                else:
                    return False
                
        if len(_stack) > 0:
            return False
        return True
        