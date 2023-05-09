import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

class Bee:
    def __init__(self, n):
        self.position = np.random.uniform(-10, 10, n)
        self.value = float('inf')

def bee_algorithm(func, n, num_bees=50, num_scouts=10, num_iterations=100, neighborhood_size=0.1):
    bees = [Bee(n) for _ in range(num_bees)]
    best_bee = None
    best_value = float('inf')

    for _ in range(num_iterations):
        for bee in bees:
            bee.value = func(bee.position)
            if bee.value < best_value:
                best_value = bee.value
                best_bee = bee

        for bee in bees[:-num_scouts]:
            new_position = bee.position + np.random.uniform(-neighborhood_size, neighborhood_size, n)
            new_position = np.clip(new_position, -10, 10)
            new_value = func(new_position)
            if new_value < bee.value:
                bee.value = new_value
                bee.position = new_position

        for bee in bees[-num_scouts:]:
            bee.position = np.random.uniform(-10, 10, n)

    return best_bee.position, best_value

if __name__ == "__main__":
    best_solution_sphere, value_sphere = bee_algorithm(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = bee_algorithm(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
