# https://leetcode.cn/problems/binary-search/description/


from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        print(f'left = {left}, right = {right}')
        middle = left + (right - left) // 2
        if target < nums[middle]:
            right = middle - 1
        elif target > nums[middle]:
            left = middle + 1
        else:
            return middle

    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(search(nums, target))
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(search(nums, target))
    nums = [-1, 0, 3, 5, 9, 12]
    target = 13
    print(search(nums, target))
