################################################################################
# Question:

# 273. Integer to English Words - Hard

# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

# Example 1:

# Input: 123
# Output: "One Hundred Twenty Three"
# Example 2:

# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Example 3:

# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Example 4:

# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

################################################################################

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        TH_MAP = ["", "Thousand", "Million", "Billion"]
        r = []
        i = 0
        if num == 0:
            return "Zero"
        while(num > 0):
            c = num % 1000
            num = num / 1000
            #print "Convert", c
            if c != 0:
                m = self.convert(c)
                m += " " + TH_MAP[i]
                r.insert(0, m)
            i += 1
        return " ".join(r).strip()
        
            
    def convert(self, c):
        s = ""
        r = 0
        LESS_THAN_20 = ["", "One","Two","Three","Four","Five","Six","Seven","Eight","Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "", "Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        i = 2
        while i >= 0:
            
            k = c / 10 ** i
            r = c % 10 ** i
            #print i, c, k ,r
            if k > 0:
                if i == 2:
                    s += LESS_THAN_20[k] + " Hundred"
                
                elif i == 1:
                    s += " " + TENS[k]
                else:
                    s += " " + LESS_THAN_20[k]
            
            if r == 0:
                break
            elif r < 20:
                s += " " + LESS_THAN_20[r]
                break
            c = r
            i -= 1
        return s.strip()
