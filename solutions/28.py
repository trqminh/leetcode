class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        w, h =  len(matrix[0]), len(matrix)
        w_i, h_i = w - 1, 0

        while w_i >= 0 and h_i < h:
            if matrix[h_i][w_i] == target:
                return True

            if matrix[h_i][w_i] > target:
                w_i -= 1
            else:
                h_i += 1

        return False


