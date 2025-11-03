import random

def fitness(x):
    return -(x**2) + 10*x + 20  # simple quadratic function

def hill_climb():
    current_x = random.uniform(0, 10)
    current_val = fitness(current_x)

    for _ in range(1000):
        new_x = current_x + random.uniform(-1, 1)
        new_val = fitness(new_x)
        if new_val > current_val:
            current_x, current_val = new_x, new_val

    return current_x, current_val

best_x, best_val = hill_climb()
print(f"Best solution found: x = {best_x:.2f}, f(x) = {best_val:.2f}")
