################################################################################
# Question:

# 17. Letter Combinations of a Phone Number - Medium


# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.

################################################################################

class Solution(object):
    
    MAP = {
        '1':['*'],
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }
    
    def combination(self, pre, _list):
        r = []
        if _list == []:
            _list = ['']
        for c in _list:
            r.append(pre + c)
        #print "Combination ->", pre, _list
        return r
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        r = []
        if len(digits) < 1:
            return r
        s = digits[0]
        #print "letterCombinations ->", digits
        rest = self.letterCombinations(digits[1:])
        #print "mix ->", self.MAP[s], rest
        for c in self.MAP[s]:
            r.extend(self.combination(c, rest))
        #print "letterCombinations Returning ->", r
        return r
  