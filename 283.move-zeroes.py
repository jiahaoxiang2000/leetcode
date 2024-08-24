#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_point = 0
        quick_point = 0
        while quick_point < len(nums):
            if nums[quick_point] != 0:
                t = nums[slow_point]
                nums[slow_point] = nums[quick_point]
                nums[quick_point] = t
                slow_point += 1
            quick_point += 1


# @lc code=end
