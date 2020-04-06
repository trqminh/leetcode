class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sums = [0] * n
        ans=1e9
        flag=False
        for i in range(n):
            sums[i] = sums[i-1] + nums[i] if i>0 else nums[i]

        for i in range(n):
            lo=i
            hi=n-1
            while lo<hi:
                mid=(lo+hi)//2
                if sums[mid]-sums[i]+nums[i] >= s:
                    hi=mid
                else:
                    lo=mid+1

            if sums[lo]-sums[i]+nums[i] >=s:
                ans=min(ans, lo-i+1)
                flag=True

        return ans if flag else 0
