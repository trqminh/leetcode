class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        i = 1
        while i < len(nums):
            if nums[i] > nums[i-1]:
                ans += 1
            else:
                del nums[i]
                i-=1

            i += 1

        return ans + 1

