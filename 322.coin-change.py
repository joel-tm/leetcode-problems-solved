#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1) #the first amount +1 is to include 0 index also 
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        if dp[amount]>amount:
              return -1
        else: return dp[amount]

sol=Solution()
op=sol.coinChange([1,2,5],12)
print(op)

        
# @lc code=end


