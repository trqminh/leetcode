class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1e10
        cur = 0
        for num in nums:
            cur += num
            ans = max(ans, cur)
            if cur < 0:
                cur = 0

        return ans

