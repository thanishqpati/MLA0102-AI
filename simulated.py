import math
import random

def objective(x):
    return -(x**2) + 10*x + 20  # same as hill climbing example

def simulated_annealing(temp, cooling_rate):
    current_x = random.uniform(0, 10)
    current_val = objective(current_x)
    best_x, best_val = current_x, current_val

    while temp > 1:
        new_x = current_x + random.uniform(-1, 1)
        new_val = objective(new_x)
        delta = new_val - current_val

        if delta > 0 or random.random() < math.exp(delta / temp):
            current_x, current_val = new_x, new_val
            if current_val > best_val:
                best_x, best_val = current_x, current_val

        temp *= cooling_rate

    return best_x, best_val

best_x, best_val = simulated_annealing(temp=1000, cooling_rate=0.95)
print(f"Best solution found: x = {best_x:.2f}, f(x) = {best_val:.2f}")
