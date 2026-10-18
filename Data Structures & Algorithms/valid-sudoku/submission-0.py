class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes =  defaultdict(list)
        rows =  defaultdict(list)
        cols = defaultdict(list)

        for r in range(9):
    
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows[r]:
                    print(f"Value {val} found in {rows[r]}")
                    return False
                else:
                    rows[r].append(val)
                    
                if val in cols[c]:
                    print(f"Value {val} found in {cols[c]}")
                    return False
                else:
                    cols[c].append(val)

                if val in boxes[(r // 3,c // 3)]:
                    print(f"Value {val} found in {boxes[(r // 3,c // 3)]}")
                    return False
                else:
                    boxes[(r // 3,c // 3)].append(val)   
        
        return True





