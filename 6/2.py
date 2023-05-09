import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

def create_population(size, n):
    return np.random.uniform(-10, 10, (size, n))

def mutation(population, F):
    donor_population = np.empty_like(population)
    for i in range(population.shape[0]):
        indices = [idx for idx in range(population.shape[0]) if idx != i]
        a, b, c = population[np.random.choice(indices, 3, replace=False)]
        donor_population[i] = a + F * (b - c)
    return donor_population

def crossover(population, donor_population, CR):
    trial_population = np.empty_like(population)
    for i in range(population.shape[0]):
        for j in range(population.shape[1]):
            if np.random.rand() < CR or j == np.random.randint(0, population.shape[1]):
                trial_population[i][j] = donor_population[i][j]
            else:
                trial_population[i][j] = population[i][j]
    return trial_population

def selection(population, trial_population, func):
    for i in range(population.shape[0]):
        if func(trial_population[i]) < func(population[i]):
            population[i] = trial_population[i]
    return population

def differential_evolution(func, n, population_size=50, num_generations=100, F=0.5, CR=0.7):
    population = create_population(population_size, n)
    for _ in range(num_generations):
        donor_population = mutation(population, F)
        trial_population = crossover(population, donor_population, CR)
        population = selection(population, trial_population, func)

    best_solution = population[np.argmin([func(ind) for ind in population])]
    return best_solution, func(best_solution)

if __name__ == "__main__":
    best_solution_sphere, value_sphere = differential_evolution(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = differential_evolution(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
