class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        invert_index = {}
        i, j, ans = 0, 0, 0

        while j < len(s):
            if s[j] in invert_index:
                i = max(i, invert_index[s[j]] + 1)

            invert_index[s[j]] = j
            ans = max(ans, j - i + 1)
            j += 1

        return ans


