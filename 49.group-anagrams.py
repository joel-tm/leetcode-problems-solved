#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        groups = defaultdict(list)
        
        for s in strs:
            # What should be the key?
            key = ''.join(sorted(s))  # Hint: sort characters
            groups[key].append(s)
        
        return list(groups.values())
            

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# @lc code=end

