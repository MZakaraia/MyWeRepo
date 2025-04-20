import random

def initialize_population(population_size, gene_length):
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(gene_length)]
        population.append(individual)
    return population

def fitness_function(individual):
    return sum(individual)

def selection(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected_indices = random.choices(range(len(population)), weights=probabilities, k=len(population))
    selected_population = [population[i] for i in selected_indices]
    return selected_population

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(population_size, gene_length, crossover_rate, mutation_rate, max_generations):
    population = initialize_population(population_size, gene_length)
    for generation in range(max_generations):
        fitness_values = [fitness_function(individual) for individual in population]
        selected_population = selection(population, fitness_values)
        new_population = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]
            if random.random() < crossover_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
    best_individual = max(population, key=fitness_function)
    return best_individual

# Example usage
population_size = 100
gene_length = 10
crossover_rate = 0.8
mutation_rate = 0.1
max_generations = 50

best_solution = genetic_algorithm(population_size, gene_length, crossover_rate, mutation_rate, max_generations)
print("Best solution:", best_solution)
print("Fitness:", fitness_function(best_solution))