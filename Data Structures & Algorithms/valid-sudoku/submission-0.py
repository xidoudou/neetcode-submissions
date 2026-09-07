class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def has_duplicates(cells):
            nums = [c for c in cells if c != "."]
            return len(nums) != len(set(nums))
        for row in board:
            if has_duplicates(row):
                return False
        
        for col in zip(*board):
            if has_duplicates(col):
                return False

        for box_row in range(3):
            for box_col in range(3):
                box = []
                for r in range(box_row*3, box_row*3 + 3):
                    for c in range(box_col*3, box_col*3 +3):
                        box.append(board[r][c])
                if has_duplicates(box):
                    return False
        return True

        


        

        