import heapq

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_x, goal_y = divmod(val - 1, 3)
                dist += abs(i - goal_x) + abs(j - goal_y)
    return dist

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    x, y = find_zero(state)
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (heuristic(start), start, []))
    visited = set()

    while pq:
        _, state, path = heapq.heappop(pq)
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if state == goal_state:
            return path + [state]

        for neighbor in get_neighbors(state):
            heapq.heappush(pq, (len(path) + heuristic(neighbor), neighbor, path + [state]))

    return None

start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = a_star(start_state)

if solution:
    print("Steps to reach goal state:")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
