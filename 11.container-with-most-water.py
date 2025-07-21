#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        max_area=0
        while l<r:
            width=r-l
            curr_h = min(height[l],height[r])
            area=width*curr_h
            #print("after",area)
            max_area=max(area,max_area)
            #print(max_area)
            if height[l]<height[r]:
                l=l+1
            elif height[l]>=height[r]:
                r-=1
        return max_area
    
print(Solution().maxArea([8,7,2,1]))
        
# @lc code=end

