class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[0 for x in range(n)] for y in range(n)]

        # base case, substring len 1
        for i in range(n):
            dp[i][i] = True

        # base case, substring len 2
        for i in range(n-1):
            dp[i][i+1] = (s[i] == s[i+1])

        for j in range(2, n):  # substring len 3 to n
            for i in range(n):
                if i + j < n:
                    dp[i][i+j] = (dp[i+1][i+j-1] and s[i] == s[i+j])

        ans, max_len = "", 0
        for i in range(n):
            for j in range(n):
                if dp[i][j] and max_len < j - i + 1:
                    ans = s[i:j+1]
                    max_len = j - i + 1

        return ans

