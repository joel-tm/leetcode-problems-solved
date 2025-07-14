#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      #  return len(nums) != len(set(nums)) 
    # if this is not equal it will return true, else false
    # if we put == then it will give false even if there are duplciates 
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
 
print(Solution().containsDuplicate([1,2,3])        )
# @lc code=end

