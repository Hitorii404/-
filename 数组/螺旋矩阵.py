# https://leetcode.cn/problems/spiral-matrix-ii/


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret_matrix = [[0] * n for _ in range(n)]
        mid = n // 2
        ret_matrix[mid][mid] = n * n

        i = 0
        j = 0
        cnt = 1
        for k in range(mid):
            while j < n - 1 - k:
                ret_matrix[i][j] = cnt
                cnt += 1
                j += 1
            while i < n - 1 - k:
                ret_matrix[i][j] = cnt
                cnt += 1
                i += 1
            while j > 0 + k:
                ret_matrix[i][j] = cnt
                cnt += 1
                j -= 1
            while i > 0 + k:
                ret_matrix[i][j] = cnt
                cnt += 1
                i -= 1
            i += 1
            j += 1

        return ret_matrix


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(5))
