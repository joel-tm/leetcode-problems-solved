#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows= defaultdict(set)
        col = defaultdict(set)
        grid= defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] =='.':
                    continue
                elif (board[r][c] in rows[r] or
                      board[r][c] in col[c] or 
                       board[r][c] in grid[(r//3,c//3)]):
                      
                    return False
                else:
                    col[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    grid[((r//3,c//3))].add(board[r][c])
        return True 
    
                

sol=Solution()
op=sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
print(op)
# @lc code=end

