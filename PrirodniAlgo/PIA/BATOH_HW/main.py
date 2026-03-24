import array
import numpy as np
from random import random, seed, shuffle

from deap import algorithms, base, creator, tools

seed(42)

import matplotlib.pyplot as plt


def biased_coin_flip(p):
    """Returns 1 with probability p and 0 with probability (1-p)."""
    return 1 if random() < p else 0

def read_input(filename="debug_10.txt"):
    with open(filename, "r") as f:
        n, max_weight = map(int, f.readline().split())
        for _ in range(n):
            price, weight = map(int, f.readline().split())
            prices.append(price)
            weights.append(weight)
    return n, max_weight

def eval_knapsack(individual):
    total_price = 0
    total_weight = 0

    for bit, price, weight in zip(individual, prices, weights):
        if bit:
            total_price += price
            total_weight += weight

    if total_weight <= max_weight:
        return total_price,

    # softer penalty
    penalty = (total_weight - max_weight) / max_weight
    return 0 * total_price * (1 -   penalty),

def repair(individual):
    total_weight = sum(w for b, w in zip(individual, weights) if b)
    
    if total_weight <= max_weight:
        return
    
    active = [i for i, b in enumerate(individual) if b]
    
    active.sort(key=lambda i: prices[i] / weights[i])  # low ratio first
    
    for i in active:
        if total_weight <= max_weight:
            break
        individual[i] = 0
        total_weight -= weights[i]

def mutate_and_repair(individual, indpb):
    tools.mutFlipBit(individual, indpb)
    repair(individual)
    return individual,


filename = "input_100.txt"
n = 0
max_weight = 0

prices = []
weights = []

n, max_weight = read_input(filename)
print(f"Number of items: {n}, Maximum weight: {max_weight}")


tournsize =  min(3, int(1 + n/100)) # Tournament size for selection (min 3 to ensure selection pressure)
indpb = 0.05 # Probability of mutating each gene in an individual
cxpb = 0.5 # Probability of crossover between pairs of individuals
mutpb = 0.35 # Probability of mutation for each individual
ngen = 100 # Number of generations to evolve



# 1. Creates a new class named "FitnessMax" that inherits from DEAP's base.Fitness.
# The weights tuple (1.0,) configures it as a single-objective MAXIMIZATION problem.
# (DEAP requires a tuple here, which is why the comma is necessary).
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# 2. Creates a new class named "Individual" that inherits from Python's memory-efficient array.array.
# The typecode='b' restricts the array to only hold 1-byte integers (perfect for 0s and 1s).
# Finally, it automatically attaches the 'FitnessMax' attribute to every new Individual created.
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# 3. Registers a new function in the toolbox named "attr_bool" that uses the biased_coin_flip function to generate
# a binary value (0 or 1) with a bias towards 1 (20% chance of being 1).
toolbox.register("attr_bool", biased_coin_flip, p=5/n) 
# 4. Registers a new function in the toolbox named "individual" that creates an Individual consisting 
# of n binary attributes (0s and 1s) using the "attr_bool" function.
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", eval_knapsack)
toolbox.register("select", tools.selTournament, tournsize=tournsize)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mutate_and_repair, indpb=indpb)





pop = toolbox.population(1000)
hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("std", np.std)
stats.register("min", np.min)
stats.register("max", np.max)

pop, log = algorithms.eaSimple(pop, toolbox, cxpb=cxpb, mutpb=mutpb, ngen=ngen, stats=stats, halloffame=hof, verbose=True)

generation = log.select("gen")
max_fitness = log.select("max")
plt.plot(generation, max_fitness, label="Max Fitness", color="red", linewidth=2)

# Make it look nice
plt.xlabel("Generation")
plt.ylabel("Total Value of Knapsack")
plt.title("Evolution of the Best Knapsack Solution")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Save the graph as a PNG file
plt.savefig("fitness_evolution" + filename.split(".")[0] + ".png", dpi=300, bbox_inches="tight")

# Show the graph!
plt.show()