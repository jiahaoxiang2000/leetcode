#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#


# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        number_maps = {}
        for num in nums:
            if num in number_maps:
                ans.append(num)
            else:
                number_maps[num] = 1
        for i in range(1, len(nums) + 1):
            if i not in number_maps:
                ans.append(i)
        return ans


# @lc code=end
