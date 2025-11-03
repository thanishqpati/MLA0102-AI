def beam_search(graph, start, goal, beam_width):
    queue = [[start]]
    while queue:
        new_queue = []
        for path in queue:
            node = path[-1]
            if node == goal:
                return path
            for neighbor, cost in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                new_queue.append((new_path, cost))
        # Sort by cost and keep top beam_width paths
        new_queue.sort(key=lambda x: x[1])
        queue = [p[0] for p in new_queue[:beam_width]]
    return None

graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 6), ('G', 1)],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

path = beam_search(graph, 'A', 'G', beam_width=2)
print("Optimal Path Found:", path)
