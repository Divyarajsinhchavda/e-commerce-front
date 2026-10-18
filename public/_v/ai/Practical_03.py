# Greedy Best-First and A* search on a weighted grid (Manhattan heuristic)
import heapq
print("Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____\n")
cost = [[1, 1, 5, 1],
        [1, 9, 5, 1],
        [1, 1, 1, 1],
        [5, 5, 1, 1]]
start, goal = (0, 0), (3, 3)

def h(p):
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])

def search(use_g):
    heap = [(h(start), 0, start, [start])]
    visited = set()
    while heap:
        _, g, node, path = heapq.heappop(heap)
        if node == goal:
            return path, g, len(visited)
        if node in visited:
            continue
        visited.add(node)
        r, c = node
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) not in visited:
                ng = g + cost[nr][nc]
                f = ng + h((nr, nc)) if use_g else h((nr, nc))
                heapq.heappush(heap, (f, ng, (nr, nc), path + [(nr, nc)]))

for name, flag in (("Greedy", False), ("A*", True)):
    path, total, expanded = search(flag)
    print(f"{name:<7} path : {path}")
    print(f"{name:<7} cost : {total}, nodes expanded: {expanded}\n")
