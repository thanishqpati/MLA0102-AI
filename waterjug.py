from collections import deque

def water_jug_problem():
    visited = set()
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        print(f"Jug1: {x}  Jug2: {y}")
        visited.add((x, y))
        if x == 2:
            print("Goal Reached: 2 gallons in Jug1")
            return
        q.extend([
            (4, y),        # Fill jug1
            (x, 3),        # Fill jug2
            (0, y),        # Empty jug1
            (x, 0),        # Empty jug2
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # Pour jug1 → jug2
            (x + min(y, 4 - x), y - min(y, 4 - x))   # Pour jug2 → jug1
        ])

water_jug_problem()
