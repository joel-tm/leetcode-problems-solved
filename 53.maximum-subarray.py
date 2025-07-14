#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            max_sum=max(curr_sum,max_sum)

            if curr_sum<0:
                curr_sum=0
        return max_sum


            
        
# @lc code=end

