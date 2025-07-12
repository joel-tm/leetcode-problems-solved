#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val: #returning all ele not equal to val
                nums[k]=nums[i]
                k=k+1
        return k
    
sol=Solution()
op=sol.removeElement([3,2,2,3],3)

    







        
# @lc code=end

