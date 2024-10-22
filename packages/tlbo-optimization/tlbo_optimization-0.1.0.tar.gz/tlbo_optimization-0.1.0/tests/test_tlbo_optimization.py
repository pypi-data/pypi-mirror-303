import unittest
from tlbo_optimization.tlbo_optimization import TLBO

class TestTLBO(unittest.TestCase):
    
    def test_optimize(self):
        def objective_function(x):
            return sum(x ** 2)

        tlbo = TLBO(population_size=10, dimensions=2, lower_bound=-5, upper_bound=5, max_iter=10, obj_func=objective_function)
        best_solution, best_fitness = tlbo.optimize()
        
        self.assertIsNotNone(best_solution)
        self.assertIsInstance(best_fitness, float)

if __name__ == '__main__':
    unittest.main()
