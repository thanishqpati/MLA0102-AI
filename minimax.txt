import math

def minimax(depth, node_index, maximizing_player, values, target_depth):
    if depth == target_depth:
        return values[node_index]
    
    if maximizing_player:
        best = -math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, False, values, target_depth)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth + 1, node_index * 2 + i, True, values, target_depth)
            best = min(best, val)
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Leaf node values:", values)
print("The optimal value is:", minimax(0, 0, True, values, 3))
