class Solution(object):
    @staticmethod
    def helper(num):
        while num >= 10:
            num = num / 10.0

        return num

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ans = ""
        tmp = {}
        a = []
        for i, num in enumerate(nums):
            x = self.helper(num)
            if x not in tmp.keys():
                tmp[x] = list()

            tmp[x].append(i)
            a.append(x)

        a.sort(reverse=True)

        for x in a:
            ans += str(nums[tmp[x]])

        return ans


#sol = Solution().largestNumber([10, 2])
#print(sol)
