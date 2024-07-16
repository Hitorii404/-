# https://leetcode.cn/problems/remove-element/description/


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print(s.removeElement(nums, val), f'nums = {nums}', sep=', ')
    print('-' * 100)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(s.removeElement(nums, val), f'nums = {nums}', sep=', ')
