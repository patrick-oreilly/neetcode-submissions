class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                if val in cols[c]:
                    return False
                else:
                    cols[c].append(val)
                
                if val in rows[r]:
                    return False
                else:
                    rows[r].append(val)
                
                if val in boxes[(r//3,c//3)]:
                    return False
                else:
                    boxes[(r//3,c//3)].append(val)

        return True