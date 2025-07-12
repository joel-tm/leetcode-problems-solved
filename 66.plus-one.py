#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            else: 
                digits[i]=0
        return [1]+digits #this only gets exectued when there is 9 alone, or just 9 
    
'''
if there are digits less than 9 it increments and returns immediately
if there is 9 it makes it 0 and goes to the next iteration(number in loop) and gets returned if its less
than 9

if there is only 9 then the return[1] + digits part  gets executed, or just 9 in loops cause none of the 
conditions in the loop are entered so it finishes the loop and goes to the next part
'''
    
sol=Solution()
op=sol.plusOne([2,9])
print(op)
# @lc code=end

