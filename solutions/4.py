class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ""

        shortest_len = len(strs[0])

        for s in strs:
            if len(s) < shortest_len:
                shortest_len = len(s)

        ans = ""
        for i in range(shortest_len):
            flag = True
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j+1][i]:
                    flag = False
                    break

            if flag:
                ans += strs[0][i]
            else:
                break

        return ans
