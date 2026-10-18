# Tic-Tac-Toe AI: Minimax vs Minimax with Alpha-Beta pruning
import math
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
count = 0

def winner(b):
    for a, c, d in LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None

def score(b, depth, alpha, beta, maxi, prune):
    global count
    count += 1
    w = winner(b)
    if w or " " not in b:
        return 10 - depth if w == "O" else depth - 10 if w else 0
    best = -math.inf if maxi else math.inf
    for i in [k for k in range(9) if b[k] == " "]:
        b[i] = "O" if maxi else "X"
        v = score(b, depth + 1, alpha, beta, not maxi, prune)
        b[i] = " "
        if maxi:
            best, alpha = max(best, v), max(alpha, v)
        else:
            best, beta = min(best, v), min(beta, v)
        if prune and beta <= alpha:
            break
    return best

def best_move(b, prune):
    moves = [i for i in range(9) if b[i] == " "]
    vals = []
    for i in moves:
        b[i] = "O"
        vals.append(score(b, 1, -math.inf, math.inf, False, prune))
        b[i] = " "
    return moves[vals.index(max(vals))]

board = list("X   O   X")                  # X to the corners, O to play
print("Board:", board)
for prune in (False, True):
    count = 0
    m = best_move(board, prune)
    tag = "Alpha-Beta" if prune else "Minimax"
    print(f"{tag:<10}: best move = cell {m}, nodes searched = {count}")
