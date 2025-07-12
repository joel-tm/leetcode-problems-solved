#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        
        return -1


sol=Solution()
op=sol.strStr(haystack="sadbut",needle="but")
print(op)       
# @lc code=end

