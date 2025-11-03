N = 4
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

colors = [0] * N

def is_safe(v, c):
    for i in range(N):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

def solve(v):
    if v == N:
        return True
    for c in range(1, N + 1):
        if is_safe(v, c):
            colors[v] = c
            if solve(v + 1):
                return True
            colors[v] = 0
    return False

if solve(0):
    print("Assigned Colors:", colors)
else:
    print("No solution exists")
