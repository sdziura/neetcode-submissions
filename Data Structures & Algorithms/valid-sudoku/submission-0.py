class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        in_rows = {i : set() for i in range(1, 10)}
        in_cols = {i : set() for i in range(1, 10)}
        in_blocks = {i : set() for i in range(1, 10)}
        for row in range(1, 10):
            block_row = ((row-1) // 3) * 3
            for col in range(1, 10):
                num = board[row-1][col-1] 
                if num == ".":
                    continue
                n_block = block_row + ((col-1) // 3) + 1
                if num in in_rows[row] or num in in_cols[col] or num in in_blocks[n_block]:
                    print(num)
                    return False
                else:
                    in_rows[row].add(num)
                    in_cols[col].add(num)
                    in_blocks[n_block].add(num)

        return True