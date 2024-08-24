#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#


# @lc code=start
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]

        n = len(nums)
        sum_ = sum(nums)
        F = sum(i * nums[i] for i in range(n))
        res = F
        for i in range(1, n):
            F += sum_ - n * nums[n - i]
            res = max(res, F)
        return res


# @lc code=end
