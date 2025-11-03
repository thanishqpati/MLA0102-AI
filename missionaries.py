from collections import deque

def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left
    if (m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0):
        return False
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False
    return True

def get_successors(state):
    m_left, c_left, boat = state
    moves = []
    if boat == 1:
        direction = -1
    else:
        direction = 1
    for m in range(3):
        for c in range(3):
            if 1 <= m + c <= 2:
                new_state = (m_left + direction*m, c_left + direction*c, 1 - boat)
                if is_valid(new_state):
                    moves.append(new_state)
    return moves

def bfs(start, goal):
    queue = deque([(start, [start])])
    while queue:
        (state, path) = queue.popleft()
        for next_state in get_successors(state):
            if next_state not in path:
                if next_state == goal:
                    return path + [next_state]
                queue.append((next_state, path + [next_state]))

start = (3, 3, 1)
goal = (0, 0, 0)
solution = bfs(start, goal)

for s in solution:
    print(s)
