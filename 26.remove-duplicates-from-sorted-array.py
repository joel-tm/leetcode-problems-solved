#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                l=l+1
                         
            else:

                continue
               


                
      
                   
        print(nums)           
        return l
    
sol=Solution()
print(sol.removeDuplicates([0,0,1,2,2,3]))

        
# @lc code=end

