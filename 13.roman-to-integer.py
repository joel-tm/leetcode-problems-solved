#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        total = 0
        roman_numerals ={
            'I':1,            
            'V':5,
            'X' :10,
            'L' :50,
            'C' :100,
            'D' :500,
            'M':1000,      
                        }
        for i in range(len(s)):
            if i+1 < len(s) and roman_numerals[s[i+1]]>roman_numerals[s[i]]:
                total=total-roman_numerals[s[i]]
            else:
                total=total+roman_numerals[s[i]]
        return total      
# @lc code=end

