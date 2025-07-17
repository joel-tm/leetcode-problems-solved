#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        count=1
        maxlength=0
        for num in a:
            curr=num
            if num -1 not in a:
                count=1
                while curr+1 in a:
                    count=count+1
                    curr=curr+1
                maxlength=max(count,maxlength)
                    
        return maxlength

        

print(Solution().longestConsecutive([100,4,200,1,3,2]))
# @lc code=end

