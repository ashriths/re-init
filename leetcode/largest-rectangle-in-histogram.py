################################################################################
# Question:

# 84. Largest Rectangle in Histogram - Hard


# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

################################################################################


import math

LOG = False

def log(*args):
    global LOG
    if LOG:
        print args

class Solution(object):
    
    def localMax(self, i, heights):
        # global LOG
        # logVal = LOG
        # LOG = len(heights) > 5
        log("localMax", heights, heights[i])
        m = heights[i]
        left = i
        right = i
        mLeft = heights[i]
        mRight = heights[i]
        while left > 0 or right < len(heights) - 1:
            log(left, right) 
            if left > 0 and heights[left - 1] >= mLeft:
                left -= 1
            elif right < len(heights) - 1 and heights[right + 1] >= mRight:
                right += 1
            elif left > 0 and right < len(heights) - 1:
                _max = max(heights[left - 1], heights[right + 1])
                if _max == heights[left - 1]:
                    left -= 1
                    mLeft = heights[left]
                else:
                    right += 1
                    mRight = heights[right]
            elif left > 0:
                left -= 1
                mLeft = heights[left]
            else:
                right += 1
                mRight = heights[right]
            log("=>", left, right )
            n = (right - left +1 ) * min(mLeft, mRight)
            log("Ar", (right - left + 1), min(mLeft, mRight))
            if n > m:
                m = n
        log("localMax =>", heights, m )
        # LOG = logVal
        return m
    
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n <= 0:
            return 0
        if n == 1:
            log(heights, heights[0])
            return heights[0]
        left = int(n/2)-1
        right = int(n/2)
        leftMax = self.largestRectangleArea(heights[:left+1])
        rightMax = self.largestRectangleArea(heights[right:])
        m = min(heights[left], heights[right])
        i = left if m == heights[left] else right
        localMax = self.localMax(i, heights)
        m = max(leftMax, rightMax, localMax)
        log(heights, m)
        return m
