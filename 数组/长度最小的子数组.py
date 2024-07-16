# https://leetcode.cn/problems/minimum-size-subarray-sum/description/


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)):
            flag = False
            sum = 0
            cnt = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                cnt += 1
                if j == len(nums) - 1 and sum < target:
                    flag = True
                if sum >= target:
                    l.append(cnt)
                    break
            if flag:
                break

        if len(l) == 0:
            return 0
        else:
            return min(l)


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
