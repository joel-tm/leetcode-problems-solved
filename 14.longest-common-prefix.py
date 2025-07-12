#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
         res=""
         for i in range(len(strs[0])):
            for j in strs[1:]:
                if i>=len(j) or j[i] != strs[0][i]:
                    return res
            res=res+strs[0][i]    
         return res

sol = Solution()
example_strs = ["fl", "f"]
print(sol.longestCommonPrefix(example_strs))  # Expected output: "fl"
    
# @lc code=end

