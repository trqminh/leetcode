class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = list()
        if x > 0:
            neg = False
        else:
            neg = True
            x = -x

        if x > 2**31:
            return 0
        res = 0
        while x:
            res = res*10 + x%10
            x/=10

        if neg:
            return -res

        return res
