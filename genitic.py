import random

def fitness(individual, target):
    return sum(1 for i, j in zip(individual, target) if i == j)

def selection(population, target):
    scores = [(ind, fitness(ind, target)) for ind in population]
    scores.sort(key=lambda x: x[1], reverse=True)
    return [ind for ind, _ in scores[:2]]

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(individual, chars):
    index = random.randint(0, len(individual) - 1)
    individual = list(individual)
    individual[index] = random.choice(chars)
    return ''.join(individual)

def genetic_algorithm(target, chars, pop_size=6, generations=100):
    population = [''.join(random.choices(chars, k=len(target))) for _ in range(pop_size)]

    for generation in range(generations):
        population = selection(population, target)
        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child, chars)
            new_pop.append(child)
        population = new_pop
        if target in population:
            print(f"Target '{target}' reached in generation {generation}!")
            return
    print("Target not reached.")

target = "HELLO"
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
genetic_algorithm(target, chars)
