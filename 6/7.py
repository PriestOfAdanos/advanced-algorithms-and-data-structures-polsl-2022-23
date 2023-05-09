import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

class Bat:
    def __init__(self, n):
        self.position = np.random.uniform(-10, 10, n)
        self.velocity = np.zeros(n)
        self.frequency = np.random.uniform(0, 1)
        self.loudness = 0.5
        self.rate = 0.5
        self.value = float('inf')

def bat_algorithm(func, n, num_bats=30, num_iterations=100, alpha=0.9, gamma=0.9):
    bats = [Bat(n) for _ in range(num_bats)]
    best_bat = None
    best_value = float('inf')

    for _ in range(num_iterations):
        for bat in bats:
            bat.frequency = np.random.uniform(0, 1)
            bat.velocity += (bat.position - best_bat.position) * bat.frequency
            new_position = bat.position + bat.velocity
            new_position = np.clip(new_position, -10, 10)
            new_value = func(new_position)

            if np.random.rand() > bat.rate and new_value < bat.value:
                bat.position = new_position
                bat.value = new_value
                bat.loudness *= alpha
                bat.rate = 1 - (1 - bat.rate) * np.exp(-gamma)

            if bat.value < best_value:
                best_value = bat.value
                best_bat = bat

    return best_bat.position, best_value

if __name__ == "__main__":
    best_solution_sphere, value_sphere = bat_algorithm(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = bat_algorithm(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
