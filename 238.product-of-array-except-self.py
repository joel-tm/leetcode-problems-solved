#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #l=[]
        l=[1]*len(nums)
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i-1]
        print("Left",l)
        right=1
        for i in range(len(nums)-1,-1,-1):
            l[i]*=right
            right*=nums[i]

        return l
        



print(Solution().productExceptSelf([3,6,7,5]))
 # @lc code=end

