import numpy as np

class TLBO:
    def __init__(self, population_size, dimensions, lower_bound, upper_bound, max_iter, obj_func):
        self.population_size = population_size  # Number of students (solutions)
        self.dimensions = dimensions  # Problem dimensions (number of variables)
        self.lower_bound = lower_bound  # Lower bounds for variables
        self.upper_bound = upper_bound  # Upper bounds for variables
        self.max_iter = max_iter  # Maximum iterations (stopping criteria)
        self.obj_func = obj_func  # Objective function to minimize

    def initialize_population(self):
        """Initialize the population within the bounds."""
        return np.random.uniform(self.lower_bound, self.upper_bound, (self.population_size, self.dimensions))

    def evaluate_population(self, population):
        """Evaluate the objective function for the entire population."""
        return np.array([self.obj_func(individual) for individual in population])

    def teaching_phase(self, population, fitness, best_student):
        """Perform the teaching phase where the teacher (best student) improves the others."""
        new_population = np.copy(population)
        mean = np.mean(population, axis=0)
        tf = np.random.randint(1, 3)  # Teaching factor can be 1 or 2
        
        for i in range(self.population_size):
            new_population[i] += np.random.rand(self.dimensions) * (best_student - tf * mean)
            new_population[i] = np.clip(new_population[i], self.lower_bound, self.upper_bound)
        
        return new_population

    def learning_phase(self, population, fitness):
        """Perform the learning phase where students learn from each other."""
        new_population = np.copy(population)
        
        for i in range(self.population_size):
            j = np.random.choice([x for x in range(self.population_size) if x != i])
            if fitness[j] < fitness[i]:
                new_population[i] += np.random.rand(self.dimensions) * (population[j] - population[i])
            else:
                new_population[i] += np.random.rand(self.dimensions) * (population[i] - population[j])
            new_population[i] = np.clip(new_population[i], self.lower_bound, self.upper_bound)
        
        return new_population

    def optimize(self):
        """Run the optimization process."""
        population = self.initialize_population()
        fitness = self.evaluate_population(population)
        best_student = population[np.argmin(fitness)]

        for _ in range(self.max_iter):
            # Teaching phase
            new_population = self.teaching_phase(population, fitness, best_student)
            new_fitness = self.evaluate_population(new_population)
            
            # Update the population if the new solutions are better
            for i in range(self.population_size):
                if new_fitness[i] < fitness[i]:
                    population[i] = new_population[i]
                    fitness[i] = new_fitness[i]

            best_student = population[np.argmin(fitness)]

            # Learning phase
            new_population = self.learning_phase(population, fitness)
            new_fitness = self.evaluate_population(new_population)
            
            for i in range(self.population_size):
                if new_fitness[i] < fitness[i]:
                    population[i] = new_population[i]
                    fitness[i] = new_fitness[i]

            best_student = population[np.argmin(fitness)]
        
        return best_student, min(fitness)

