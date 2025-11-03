colors = ['Red', 'Green', 'Blue']

states = ['A', 'B', 'C', 'D']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

solution = {}

def is_valid(state, color):
    for neighbor in neighbors[state]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def csp(state_index):
    if state_index == len(states):
        return True
    state = states[state_index]
    for color in colors:
        if is_valid(state, color):
            solution[state] = color
            if csp(state_index + 1):
                return True
            del solution[state]
    return False

if csp(0):
    print("Solution Found:")
    for s in states:
        print(f"{s} -> {solution[s]}")
else:
    print("No valid coloring found.")
