import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqnum = math.sqrt(num)
        return int(sqnum) * int(sqnum) == num