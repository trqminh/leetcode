class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while n >= 0:
            n -= i
            i += 1

        return i - 2
