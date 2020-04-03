class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            while lo<hi and nums[lo]==nums[lo+1]:
                lo+=1

            while lo<hi and nums[hi-1]==nums[hi]:
                hi-=1

            mid=(lo+hi)//2
            if nums[mid]==target:
                return True

            if nums[mid] > target:
                if nums[mid] < nums[lo] or nums[lo] <= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[lo] <= nums[mid] or nums[lo] > target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False
