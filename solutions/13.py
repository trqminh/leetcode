class Solution(object):
    def binary_search(self, nums, target, is_find_leftmost):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (is_find_leftmost and nums[mid] == target):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [-1, -1]
        left = self.binary_search(nums, target, is_find_leftmost=True)

        if left >= len(nums) or nums[left] != target:
            return ans

        return [left, self.binary_search(nums, target, is_find_leftmost=False) - 1]
