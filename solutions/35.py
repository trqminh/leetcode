class Solution(object):
    def swap(self, nums, i, j):
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = 0, n - 1
        for i in range(n):
            while nums[i] == 2 and i < r:
                self.swap(nums, i, r)
                r -= 1

            while nums[i] == 0 and i > l:
                self.swap(nums, i, l)
                l += 1

        return nums

