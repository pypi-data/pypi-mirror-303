=================
tlbo_optimization
=================

.. image:: https://img.shields.io/pypi/v/tlbo_optimization.svg
   :target: https://pypi.python.org/pypi/tlbo_optimization

.. image:: https://img.shields.io/travis/smbd1368/tlbo_optimization.svg
   :target: https://travis-ci.com/smbd1368/tlbo_optimization

Teaching-Learning-Based Optimization (TLBO) algorithm
=====================================================

Overview
--------

The TLBO algorithm is a population-based optimization technique inspired by the teaching-learning process. This package provides an easy-to-use implementation of TLBO for optimizing various objective functions.

Features
--------

- Simple and intuitive interface for using TLBO
- Supports multiple objective functions
- Customizable parameters such as population size, number of dimensions, and bounds
- Efficient optimization for various types of problems

Installation
------------

You can install the package using pip:

.. code-block:: bash

    pip install tlbo-optimization

Example
-------

Here is an example of how to use the TLBO algorithm:

.. code-block:: python

    from tlbo_optimization.tlbo_optimization import TLBO

    def objective_function(x):
        return sum(x ** 2)

    tlbo = TLBO(
        population_size=30,
        dimensions=5,
        lower_bound=-10,
        upper_bound=10,
        max_iter=100,
        obj_func=objective_function
    )

    best_solution, best_fitness = tlbo.optimize()

    print(f"Best solution: {best_solution}")
    print(f"Best fitness: {best_fitness}")

Contributing
------------

Contributions are welcome! Please read the `CONTRIBUTING.rst` for details on how to contribute.

License
-------

This project is licensed under the GNU General Public License v3.

