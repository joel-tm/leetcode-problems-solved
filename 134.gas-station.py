#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        if sum(gas)<sum(cost):
            return -1 
        res=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]

            if total<0:
                total=0
                res=i+1
        return res
            

sol=Solution()
op=sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
print(op)

        
# @lc code=end

