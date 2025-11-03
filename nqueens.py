import random

N = 8

def random_state():
    return [random.randint(0, N-1) for _ in range(N)]

def cost(state):
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                attacks += 1
    return attacks

def get_neighbors(state):
    neighbors = []
    for col in range(N):
        for row in range(N):
            if state[col] != row:
                neighbor = list(state)
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climb():
    current = random_state()
    while True:
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=lambda x: cost(x))
        if cost(next_state) >= cost(current):
            return current
        current = next_state

solution = hill_climb()
print("Final State:", solution)
print("Final Cost (attacking pairs):", cost(solution))
