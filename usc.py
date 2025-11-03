from queue import PriorityQueue

def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    visited = set()
    cost = {start: 0}
    parent = {start: None}

    while not pq.empty():
        current_cost, current_node = pq.get()
        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            break

        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                pq.put((new_cost, neighbor))
                parent[neighbor] = current_node

    path = []
    node = goal
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, cost[goal]

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 3), ('E', 5)],
    'C': [('F', 2)],
    'D': [('F', 1), ('E', 1)],
    'E': [('F', 2)],
    'F': []
}

path, total_cost = uniform_cost_search(graph, 'A', 'F')
print("Optimal Path:", path)
print("Total Cost:", total_cost)
