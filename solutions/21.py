class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        r=nums[0]
        for i in range(1,n):
            r = r ^ nums[i]
        return r
