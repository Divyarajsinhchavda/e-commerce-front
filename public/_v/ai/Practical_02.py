# Robot path finding on a grid using BFS, DFS and DLS
from collections import deque
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
grid = ["S.#..",
        ".##.#",
        "....G",
        "#.#.."]
R, C = len(grid), len(grid[0])
start, goal = (0, 0), (2, 4)

def moves(r, c):
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] != "#":
            yield nr, nc

def bfs():
    q, seen = deque([[start]]), {start}
    while q:
        path = q.popleft()
        if path[-1] == goal:
            return path
        for n in moves(*path[-1]):
            if n not in seen:
                seen.add(n)
                q.append(path + [n])

def dfs(path, seen):
    if path[-1] == goal:
        return path
    for n in moves(*path[-1]):
        if n not in seen:
            res = dfs(path + [n], seen | {n})
            if res:
                return res

def dls(path, limit):
    if path[-1] == goal:
        return path
    if limit == 0:
        return None
    for n in moves(*path[-1]):
        if n not in path:
            res = dls(path + [n], limit - 1)
            if res:
                return res

for name, p in [("BFS", bfs()), ("DFS", dfs([start], {start})),
                ("DLS (limit 4)", dls([start], 4)),
                ("DLS (limit 6)", dls([start], 6))]:
    print(f"{name:<14}:", p if p else "No path within limit",
          f"({len(p) - 1} moves)" if p else "")
