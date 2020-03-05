class Solution(object):
    def iscycle(self, pre_dict, index, target):
        if index not in pre_dict.keys() or len(pre_dict[index]) <= 0:
            return False

        if target in pre_dict[index]:
            return True

        for course in pre_dict[index]:
            if self.iscycle(pre_dict, course, target):
                return True

        return False


    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prerequisites_dict = {}
        for pre in prerequisites:
            if pre[0] not in prerequisites_dict.keys():
                prerequisites_dict[pre[0]] = []

            prerequisites_dict[pre[0]].append(pre[1])

            if self.iscycle(prerequisites_dict, pre[1], pre[0]):
                return False


        return True
