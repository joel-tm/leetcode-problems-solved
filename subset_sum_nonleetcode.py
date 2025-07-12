from typing import List

class Solution:
    def subsetSum(self, nums: List[int], target: int) -> bool:
        # DP approach
        # dp[i] represents whether target sum i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Sum 0 is always possible (empty subset)
        
        # For each number in the array
        for num in nums:
            # Traverse from target to num (backwards to avoid using same element twice)
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
    


# Test cases
sol = Solution()

# Test case 1: {3, 34, 4, 12, 5, 2}, sum = 9
nums1 = [3, 34, 4, 12, 5, 2]
target1 = 9
print(f"Input: {nums1}, target: {target1}")
print(f"Output: {sol.subsetSum(nums1, target1)}")  # True (4 + 5 = 9)

# Test case 2: {3, 34, 4, 12, 5, 2}, sum = 30
nums2 = [3, 34, 4, 12, 5, 2]
target2 = 30
print(f"Input: {nums2}, target: {target2}")
print(f"Output: {sol.subsetSum(nums2, target2)}")  # False

# Test case 3: Edge case
nums3 = [1, 2, 3]
target3 = 6
print(f"Input: {nums3}, target: {target3}")
print(f"Output: {sol.subsetSum(nums3, target3)}")  # True (1 + 2 + 3 = 6)
