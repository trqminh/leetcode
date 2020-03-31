class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums)-1
        x = nums[hi]
        while lo<hi:
            mid=(lo+hi)//2
            if nums[mid]>nums[mid+1]:
                return min(nums[0], nums[mid+1])
            elif nums[mid]<nums[mid+1] and nums[mid]<x:
                hi=mid
            else:
                lo=mid+1

        return nums[0]

