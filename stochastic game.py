def expectiminimax(node, depth, player):
    if depth == 0 or node not in tree:
        return node
    
    if player == "MAX":
        return max([expectiminimax(child, depth - 1, "MIN") for child in tree[node]])
    elif player == "MIN":
        return min([expectiminimax(child, depth - 1, "CHANCE") for child in tree[node]])
    else:
        values = [expectiminimax(child, depth - 1, "MAX") for child in tree[node]]
        prob = [0.5, 0.5]  # equal probability for simplicity
        return sum(v * p for v, p in zip(values, prob))

tree = {
    "A": ["B", "C"],
    "B": [3, 12],
    "C": [8, 2]
}

print("Expectiminimax Value:", expectiminimax("A", 3, "MAX"))
