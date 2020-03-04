class Solution(object):
    def iscycle(pre_dict, index, target):
        if len(pre_dict[index]) <= 0:
            return False

        if target in pre_dict[index]:
            return True

        for course in pre_dict[target]:
            if iscycle(pre_dict, )


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
