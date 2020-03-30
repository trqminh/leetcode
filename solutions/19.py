class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if mid-1<0:
                return lo if nums[lo] >= nums[hi] else hi
            if nums[mid-1] <= nums[mid] >= nums[mid+1]:
                return mid
            if nums[mid-1] <= nums[mid] <= nums[mid+1]:
                lo = mid + 1
            else:
                hi = mid

        return lo
