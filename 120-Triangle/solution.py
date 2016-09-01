class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        resultl = triangle[n-1][:]
        for i in range(n-2, -1, -1):
            length = len(triangle[i])
            for j in range(length):
                resultl[j] = triangle[i][j] + min(resultl[j], resultl[j+1])
        return resultl[0]