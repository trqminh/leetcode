class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (hi + lo) // 2
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1


        if nums[lo - 1] != target:
            return lo

        return lo - 1
