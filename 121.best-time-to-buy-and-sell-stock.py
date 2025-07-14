#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=float('inf')
        max_price=0
        for price in prices:
            if price<min:
                min=price
            else:
                profit=price-min
                print("in",profit)
                max_price=max(profit,max_price)


        return max_price

sol=Solution()
op=sol.maxProfit([7,1,5,3,6,4])
#print(op)

        
# @lc code=end

