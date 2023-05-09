import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

def objective_function(x, func):
    return func(x)

def create_population(size, n):
    return np.random.uniform(-10, 10, (size, n))

def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    crossover_point = np.uint8(offspring_size[1] / 2)

    for k in range(offspring_size[0]):
        parent1_idx = k % parents.shape[0]
        parent2_idx = (k + 1) % parents.shape[0]
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    for idx in range(offspring_crossover.shape[0]):
        random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, np.random.randint(0, offspring_crossover.shape[1], 1)] += random_value
    return offspring_crossover

def genetic_algorithm(func, n, num_generations=100, population_size=50):
    population = create_population(population_size, n)
    best_outputs = []

    for generation in range(num_generations):
        fitness = [objective_function(p, func) for p in population]
        best_outputs.append(np.min(fitness))
        parents = population[np.argsort(fitness)[:int(population_size * 0.1)]]
        offspring_crossover = crossover(parents, offspring_size=(population_size - parents.shape[0], n))
        offspring_mutation = mutation(offspring_crossover)
        population[0:parents.shape[0], :] = parents
        population[parents.shape[0]:, :] = offspring_mutation

    best_solution = population[np.argmin(fitness)]
    return best_solution, objective_function(best_solution, func)

if __name__ == "__main__":
    best_solution_sphere, value_sphere = genetic_algorithm(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = genetic_algorithm(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
