class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        lo = 0
        hi = n - 1
        h_index = 0
        while lo<=hi:
            mid=(lo+hi)//2
            if n - mid <= citations[mid]:
                hi = mid - 1
                h_index = max(h_index, n - mid)
            else:
                lo = mid + 1


        return h_index
