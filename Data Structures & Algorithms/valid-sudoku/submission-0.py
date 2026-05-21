class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 10 for _ in range(9)]
        col = [[0] * 10 for _ in range(9)]
        square = [[0] * 10 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    val = int(board[i][j])
                else:
                    continue
                if (row[i][val] == 1 or col[j][val] == 1 
                    or square[(i//3)*3+(j//3)][val]) == 1:
                    return False
                row[i][val] = 1 
                col[j][val] = 1
                square[(i//3)*3+(j//3)][val] = 1
        return True