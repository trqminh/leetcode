class Solution(object):
    def binary_search(self, numbers, search_target, lo, hi):
        while lo<hi:
            mid=(lo+hi)//2
            if numbers[mid]==search_target:
                return mid
            if numbers[mid]<search_target:
                lo=mid+1
            else:
                hi=mid

        return -1

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        for i,num in enumerate(numbers):
            idx = self.binary_search(numbers, target-num, i+1, n)
            if idx!=-1:
                return [i+1, idx+1]

        return None

