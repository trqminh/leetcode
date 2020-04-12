class Solution(object):
    def check(self, A, B, k):
        hash_map = {}
        for i in range(len(A)):
            if i + k <= len(A):
                hash_map[str(A[i:i+k])] = True

        for j in range(len(B)):
            if j + k <= len(B):
                if str(B[j:j+k]) in hash_map.keys():
                    return True

        return False

    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lo = 0
        hi = min(len(A), len(B)) + 1

        while lo < hi:
            mid = (lo + hi) // 2
            if self.check(A, B, mid):
                lo = mid + 1
            else:
                hi = mid

        return lo - 1
