# Sudoku (4x4) as a Constraint Satisfaction Problem using backtracking
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
board = [[1, 0, 0, 0],
         [0, 0, 3, 0],
         [0, 4, 0, 0],
         [0, 0, 0, 2]]

def valid(r, c, v):
    if v in board[r] or v in [board[i][c] for i in range(4)]:
        return False
    br, bc = r // 2 * 2, c // 2 * 2                  # 2x2 box constraint
    return all(board[i][j] != v for i in range(br, br + 2)
               for j in range(bc, bc + 2))

steps = 0
def solve():
    global steps
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:                     # variable
                for v in range(1, 5):                # domain
                    if valid(r, c, v):
                        board[r][c] = v
                        steps += 1
                        if solve():
                            return True
                        board[r][c] = 0              # backtrack
                return False
    return True

print("Puzzle:")
for row in board:
    print("  ", " ".join(str(x) if x else "." for x in row))
if solve():
    print("\nSolved in", steps, "assignments:")
    for row in board:
        print("  ", " ".join(map(str, row)))
