import numpy as np

def sphere(x):
    return np.sum(np.square(x))

def sum_squares(x):
    return np.sum((i + 1) * x[i] ** 2 for i in range(len(x)))

class Particle:
    def __init__(self, n):
        self.position = np.random.uniform(-10, 10, n)
        self.velocity = np.random.uniform(-1, 1, n)
        self.best_position = self.position
        self.best_value = float('inf')

    def update_velocity(self, global_best, w=0.7, c1=2, c2=2):
        inertia = w * self.velocity
        cognitive = c1 * np.random.rand() * (self.best_position - self.position)
        social = c2 * np.random.rand() * (global_best - self.position)
        self.velocity = inertia + cognitive + social

    def update_position(self):
        self.position = self.position + self.velocity

def particle_swarm_optimization(func, n, swarm_size=30, num_iterations=100):
    swarm = [Particle(n) for _ in range(swarm_size)]
    global_best = None
    global_best_value = float('inf')

    for _ in range(num_iterations):
        for particle in swarm:
            value = func(particle.position)
            if value < particle.best_value:
                particle.best_value = value
                particle.best_position = particle.position
            if value < global_best_value:
                global_best_value = value
                global_best = particle.position

        for particle in swarm:
            particle.update_velocity(global_best)
            particle.update_position()

    return global_best, global_best_value

if __name__ == "__main__":
    best_solution_sphere, value_sphere = particle_swarm_optimization(sphere, n=2)
    best_solution_sum_squares, value_sum_squares = particle_swarm_optimization(sum_squares, n=2)

    print("Sphere Function:")
    print("Best solution:", best_solution_sphere)
    print("Best solution value:", value_sphere)

    print("\nSum of Squares Function:")
    print("Best solution:", best_solution_sum_squares)
    print("Best solution value:", value_sum_squares)
