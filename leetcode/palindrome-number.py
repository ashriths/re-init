################################################################################
# Question:

# 9. Palindrome Number
# Easy
# 1050
# 1117


# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?

################################################################################

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while y < x:
            d, r = divmod(x, 10)
            y = y * 10 + r 
            x = x / 10
        return x == y or x == (y/10)
            
            
            
        