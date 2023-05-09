import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

class Firefly:
    def __init__(self, n):
        self.position = np.random.uniform(-10, 10, n)
        self.intensity = float('inf')

def firefly_algorithm(func, n, num_fireflies=30, num_iterations=100, absorption=1):
    fireflies = [Firefly(n) for _ in range(num_fireflies)]
    best_firefly = None
    best_value = float('inf')

    for _ in range(num_iterations):
        for firefly in fireflies:
            firefly.intensity = func(firefly.position)
            if firefly.intensity < best_value:
                best_value = firefly.intensity
                best_firefly = firefly

        for i in range(num_fireflies):
            for j in range(num_fireflies):
                if fireflies[i].intensity > fireflies[j].intensity:
                    distance = np.linalg.norm(fireflies[i].position - fireflies[j].position)
                    attractiveness = np.exp(-absorption * distance)
                    fireflies[i].position += attractiveness * (fireflies[j].position - fireflies[i].position) + np.random.uniform(-1, 1, n)
                    fireflies[i].position = np.clip(fireflies[i].position, -10, 10)

    return best_firefly.position, best_value

if __name__ == "__main__":
    best_solution_sphere, value_sphere = firefly_algorithm(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = firefly_algorithm(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
