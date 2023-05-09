import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

def create_population(size, n):
    return np.random.uniform(-10, 10, (size, n))

def levy_flight(Lambda):
    sigma1 = np.power((np.gamma(1 + Lambda) * np.sin(np.pi * Lambda / 2)) / np.gamma((1 + Lambda) / 2) * np.power(2, (Lambda - 1) / 2), 1 / Lambda)
    sigma2 = 1
    u = np.random.normal(0, sigma1, size=(n,))
    v = np.random.normal(0, sigma2, size=(n,))
    step = u / np.power(np.abs(v), 1 / Lambda)

    return 0.01 * step

def cuckoo_search(func, n, population_size=20, num_generations=100, pa=0.25):
    population = create_population(population_size, n)
    fitness = np.apply_along_axis(func, 1, population)
    best_idx = np.argmin(fitness)
    best = population[best_idx]

    for _ in range(num_generations):
        for i in range(population_size):
            levy = levy_flight(1.5)
            new_solution = population[i] + levy
            new_solution = np.clip(new_solution, -10, 10)
            if func(new_solution) < func(population[i]):
                population[i] = new_solution
                if func(population[i]) < func(best):
                    best = population[i]

        for i in range(population_size):
            if np.random.rand() < pa:
                population[i] = create_population(1, n)
                if func(population[i]) < func(best):
                    best = population[i]

    return best, func(best)

if __name__ == "__main__":
    best_solution_sphere, value_sphere = cuckoo_search(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = cuckoo_search(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
