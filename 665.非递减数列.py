#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#


# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        cnt = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
                if cnt > 1:
                    return False
                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
        return True


# @lc code=end
