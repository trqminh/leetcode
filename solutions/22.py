class Solution(object):
    def binary_search(self, nums, lo, hi):
        if lo == hi or nums[lo] < nums[hi]:
            return nums[lo]

        mid=(lo+hi)//2
        if nums[mid]>nums[lo]:
            return self.binary_search(nums, mid+1, hi)
        elif nums[mid]<nums[lo]:
            return self.binary_search(nums, lo, mid)
        else:
            return min(self.binary_search(nums, mid+1,hi), self.binary_search(nums, lo, mid))

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hi=len(nums)-1
        if hi == 0 or nums[0] < nums[hi]:
            return nums[0]

        return self.binary_search(nums, 0, hi)

