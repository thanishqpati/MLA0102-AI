import math
import random

def cost_function(schedule):
    conflicts = 0
    for i in range(len(schedule)-1):
        if schedule[i] == schedule[i+1]:
            conflicts += 1
    return conflicts

def random_neighbor(schedule):
    neighbor = schedule[:]
    i = random.randint(0, len(schedule)-1)
    neighbor[i] = random.randint(1, 3)
    return neighbor

def simulated_annealing(schedule, temp, cooling_rate):
    current = schedule
    current_cost = cost_function(current)
    best = current
    best_cost = current_cost

    while temp > 1:
        new = random_neighbor(current)
        new_cost = cost_function(new)
        delta = new_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_cost = new, new_cost
        if current_cost < best_cost:
            best, best_cost = current, current_cost
        temp *= cooling_rate
    return best, best_cost

initial_schedule = [random.randint(1, 3) for _ in range(6)]
print("Initial Schedule:", initial_schedule)

best_schedule, best_cost = simulated_annealing(initial_schedule, temp=1000, cooling_rate=0.95)
print("Best Schedule:", best_schedule)
print("Best Cost:", best_cost)
