#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for i in s:
            if i in dict:
                stack.append(i)
                #print(stack)
            else:
                if not stack or dict[stack.pop()] != i: #the m[stack.pop] returns a value and
                    return False

        return not stack

sol = Solution()

print(sol.isValid("{[]}"))    # True
# @lc code=end

