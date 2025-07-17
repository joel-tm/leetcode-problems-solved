#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l,r=0,len(num)-1

        while l<r:
            curr_sum=num[l]+num[r]

            if curr_sum==target:
                return [l+1,r+1]
            elif curr_sum<target:
                l+=1
            else:
                r-=1

print(Solution().twoSum([2,7,11,15],9))
        
# @lc code=end

