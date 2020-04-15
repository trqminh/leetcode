class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        intersection = []

        i1, i2 = 0, 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                intersection.append(nums1[i1])
                i1+=1
                i2+=1
                while i1 < len(nums1) and i2 < len(nums2) and nums1[i1] == nums2[i2]:
                    if nums1[i1] != nums1[i1 - 1]:
                        intersection.append(nums1[i1])
                    i1+=1
                    i2+=1

            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1


        return intersection
