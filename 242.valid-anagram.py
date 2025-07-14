#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
    


        

sol=Solution()
op=sol.isAnagram("anagram","nagaram")
print(op)        
# @lc code=end

