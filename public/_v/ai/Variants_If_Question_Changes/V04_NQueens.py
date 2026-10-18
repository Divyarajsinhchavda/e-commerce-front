# N-Queens as a Constraint Satisfaction Problem using backtracking
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
N = 6                                   # change N for a different board size
solutions = []

def safe(cols, row, col):               # constraints: no same column, no same diagonal
    for r, c in enumerate(cols):
        if c == col or abs(c - col) == row - r:
            return False
    return True

def place(cols):
    row = len(cols)
    if row == N:
        solutions.append(cols[:])
        return
    for col in range(N):                # domain = columns 0..N-1
        if safe(cols, row, col):
            cols.append(col)
            place(cols)
            cols.pop()                  # backtrack

place([])
print(f"{N}-Queens: {len(solutions)} solutions found")
print("First solution (row -> column):", solutions[0])
for r in range(N):
    print("  ", " ".join("Q" if solutions[0][r] == c else "." for c in range(N)))
