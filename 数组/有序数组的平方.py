# https://leetcode.cn/problems/squares-of-a-sorted-array/description/


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = list(map(lambda num: num ** 2, nums))
        new_list.sort()
        return new_list


if __name__ == '__main__':
    s = Solution()
    nums = [-4, -1, 0, 3, 10]
    print(s.sortedSquares(nums))
    nums = [-7, -3, 2, 3, 11]
    print(s.sortedSquares(nums))
