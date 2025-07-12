#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1), len(text2)
        @cache
        def longest(i,j):
            if i==m or j==n:
                return 0
            elif text1[i]==text2[j]:
                return 1+longest(i+1,j+1)
            else:
                return max(longest(i,j+1),longest(i+1,j))
        
        return longest(0,0)
        
        
                        


sol=Solution()
op=sol.longestCommonSubsequence("gators","agars")
print(op)
# @lc code=end

