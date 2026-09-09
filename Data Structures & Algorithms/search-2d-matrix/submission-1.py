class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        sort_matrix = []
        for value in matrix:
            sort_matrix += value
        
        l, r = 0, len(sort_matrix) -1

        while l <= r:
            m = (l+r) //2
            if sort_matrix[m] < target:
                l = m + 1
            elif sort_matrix[m] > target:
                r = m - 1
            else:
                return True
        return False
        