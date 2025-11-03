from queue import PriorityQueue

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('F', 1), ('E', 1)],
    'E': [('F', 2)],
    'F': []
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0, 'F': 0}

def a_star(start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {start: None}

    while not pq.empty():
        _, current = pq.get()
        if current == goal:
            break
        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost
            if temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f = temp_g + heuristic[neighbor]
                pq.put((f, neighbor))
                parent[neighbor] = current

    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path, g_cost[goal]

path, cost = a_star('A', 'F')
print("Optimal Path:", path)
print("Total Cost:", cost)
