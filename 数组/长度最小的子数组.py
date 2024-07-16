# https://leetcode.cn/problems/minimum-size-subarray-sum/description/


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = 10 ** 5 + 1
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                sub_length = j - i + 1
                if sub_length < ret:
                    ret = sub_length
                sum -= nums[i]
                i += 1

        if ret == 10 ** 5 + 1:
            ret = 0
        return ret


if __name__ == '__main__':
    s = Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(s.minSubArrayLen(target, nums))
    print('-' * 100)

    target = 4
    nums = [1, 4, 4]
    print(s.minSubArrayLen(target, nums))
    print('-' * 100)

    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(s.minSubArrayLen(target, nums))
    print('-' * 100)
