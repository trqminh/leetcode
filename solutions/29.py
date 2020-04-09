class Solution(object):
    def recursive_search(self, nums, prev, cur_pos):
        if cur_pos == len(nums):
            return 0

        taken_prev = 0
        if nums[cur_pos] > prev:
            taken_prev = 1 + self.recursive_search(nums, nums[cur_pos], cur_pos + 1)

        not_taken_prev = self.recursive_search(nums, prev, cur_pos + 1)
        return max(taken_prev, not_taken_prev)

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.recursive_search(nums, -1e9, 0)
