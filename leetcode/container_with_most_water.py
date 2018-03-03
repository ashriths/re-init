class Solution(object):
    
    def calc_area(self, left, right, height):
        return (right - left) * min(height[left], height[right])
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        _max = 0
        _max_index = None
        while left < right:
            area = self.calc_area(left, right, height)
            if area > _max:
                _max = area
                _max_index = (left, right)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return _max       