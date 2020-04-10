class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 0:
            return 0
        dp = [0]*n
        dp[0] = 1
        for i in range(1, n):
            maxval = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])

            dp[i] = 1 + maxval

        ans = 0
        for dp_i in dp:
            ans = max(ans, dp_i)

        return ans
