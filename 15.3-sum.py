#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=sorted(nums)
        #l,r=1, len(nums)-1
        res=[]
        for i,j in enumerate(a):
            l,r=i+1, len(nums)-1
            if i>0 and a[i]==a[i-1]:
                continue

            while l<r:
                threesum= j+a[l]+a[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l=l+1
                else:
                    res.append([j,a[l],a[r]])
                    while l<r and a[l] ==a[l+1]:
                        l+=1
                    while l<r and a[r]==a[r-1]:
                        r-=1
                    l=l+1
                    r-=1
        return res
#-4,-1,-1,0,1,2            

print(Solution().threeSum([-1,0,1,2,-1,-4]))        
# @lc code=end

