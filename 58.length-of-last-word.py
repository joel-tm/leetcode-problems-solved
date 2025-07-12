#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,j=len(s)-1,0
        while s[i]==" ":
            i-=1
        while s[i] !=" " and i>=0:
            j+=1
            i-=1
        return j
    



sol=Solution()
op=sol.lengthOfLastWord("joyboy is  luffy ")
print(op)

            
        
# @lc code=end

