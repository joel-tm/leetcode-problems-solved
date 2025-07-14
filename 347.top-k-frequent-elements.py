#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h={}

        for n in nums:
            h[n] = h.get(n,0)+1
        sor=sorted(h.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
              res.append(sor[i][0])
        return res

print(Solution().topKFrequent([1,1,1,2,2,3,4,4,4,4],2))     
# @lc code=end

