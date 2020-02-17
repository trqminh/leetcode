class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        hashmap = {}
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                su = nums[i] + nums[j]
                if su not in hashmap:
                    hashmap[su] = []

                hashmap[su].append((i, j))

        is_used = []
        for i in range(len(nums)):
            su = -nums[i]
            if su in hashmap:
                m = hashmap[su][-1][0]
                n = hashmap[su][-1][1]
                if m != i and n != i:
                    ans.append([nums[i], nums[m], nums[n]])


                hashmap[su].pop()
                if len(hashmap[su]) <= 0:
                    hashmap.pop(su, None)

        return ans

