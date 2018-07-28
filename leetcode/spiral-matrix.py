class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        out = []
        n = len(matrix)
        if not n:
            return out
        m = len(matrix[0])
        left ,right, top, bottom = 0, m-1, 0, n-1
        while left <= right and top <= bottom:
            print left, right , top, bottom
            for i in xrange(left, right+1):
                out.append(matrix[top][i])
            for j in xrange(top+1, bottom+1):
                out.append(matrix[j][right])
            for k in reversed(xrange(left, right)):
                if top < bottom:
                    out.append(matrix[bottom][k])
            for l in reversed(xrange(top+1, bottom)):
                if left < right:
                    out.append(matrix[l][left])
            left, right, top, bottom = left + 1, right -1 , top + 1, bottom -1
        return out
