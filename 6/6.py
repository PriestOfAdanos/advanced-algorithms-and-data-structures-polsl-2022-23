import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

class Ant:
    def __init__(self, n):
        self.position = np.random.randint(0, 100, n)
        self.value = float('inf')

def ant_algorithm(func, n, num_ants=50, num_iterations=100, alpha=1, beta=5, rho=0.5):
    grid = np.zeros((100, 100))
    ants = [Ant(n) for _ in range(num_ants)]
    best_ant = None
    best_value = float('inf')

    for _ in range(num_iterations):
        for ant in ants:
            possible_moves = [ant.position + np.array([dx, dy]) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
            possible_moves = [move for move in possible_moves if move[0] >= 0 and move[1] >= 0 and move[0] < 100 and move[1] < 100]
            pheromone_values = [grid[move[0], move[1]] for move in possible_moves]
            total = sum(pheromone_values)

            if total == 0:  # If all pheromone values are zero
                probabilities = [1 / len(possible_moves) for _ in possible_moves]  # Assign equal probabilities
            else:
                probabilities = [pheromone / total for pheromone in pheromone_values]
            
            ant.position = possible_moves[np.random.choice(len(possible_moves), p=probabilities)]
            ant.value = func(ant.position / 10 - 5)

            if ant.value < best_value:
                best_value = ant.value
                best_ant = ant

        for ant in ants:
            grid[ant.position[0], ant.position[1]] += 1 / ant.value

        grid *= (1 - rho)

    return best_ant.position / 10 - 5, best_value

if __name__ == "__main__":
    best_solution_sphere, value_sphere = ant_algorithm(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = ant_algorithm(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
