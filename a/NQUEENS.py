
# N Queens Problem

def solveNQueens(n):
    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]
    
    def issafe(row, col):
        return col not in cols and row-col not in posDiag and row+col not in negDiag
    
    def backtrack(row):
        if row == n:
            solutions.append([''.join(i) for i in board])
            return
        for col in range(n):
            if issafe(row, col):
                cols.add(col)
                posDiag.add(row-col)
                negDiag.add(row+col)
                
                board[row][col] = "Q"
                backtrack(row+1)
                board[row][col] = "."
                
                cols.remove(col)
                posDiag.remove(row-col)
                negDiag.remove(row+col)
    
    cols = set()
    posDiag = set()
    negDiag = set()
    
    backtrack(0)
    
    return solutions

n = 4
solutions = solveNQueens(n)
print(f'Number of solutions: {len(solutions)}')
for i in solutions:
    for j in i: print(j)
    print()
    