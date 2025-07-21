#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
             return 0
        l=0
        r=len(height)-1
        leftmax,rightmax = height[l],height[r]
        res=0
        while l<r:
            if height[l]<height[r]:
                l=l+1
                leftmax=max(leftmax,height[l])
                res+=leftmax -height[l]
            else:
                r-=1
                rightmax=max(rightmax,height[r])
                res+=rightmax-height[r]
        return res

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        
# @lc code=end

