class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pro = 1
        length = len(nums)
        out = [1] * length
        for key in xrange(length-1, -1, -1):
            pro = pro * nums[key]
            out[key] = pro
        pro = 1
        for key in xrange(length):
            right = out[key+1] if key < len(nums)-1 else 1
            out[key] = pro * right
            pro = pro * nums[key]
        return out
