class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        invert_idx = {}
        for idx, num in enumerate(nums):
            n = target - num
            if n not in invert_idx:
                invert_idx[num] = idx
            else:
                return [idx, invert_idx[n]]

        return "No answer"
