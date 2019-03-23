'''
Author  : Gu-hwan Bae
Summary : A linear programming problem, standard maximization problem.
          In this tutorial, we are to find the maximum value of the objective
          function. All the variables are constrained to be non-negative.
          All constraints inequalities have less than operations.
'''

import gula.simplex as gsimplex
import numpy as np

'''
Consider a cafe which produces three types of beverage, Cafe Mocha, Caffe Latte,
Chocolate milk. To make each cup of beverage, following under recipes.

Each cup of Cafe Mocah requires 2 shots of espresso, 4 oz of milk, 1 oz of chocolate cream.
Each cup of Caffe Latte requires 2 shots of espresso and 4.5 oz of milk.
Each cup of Chocholate milk requires 5 oz of milk and 2.5 oz of chocholate cream.

The cafe has a total of 120 shots of espresso, 300 oz of milk and 80 oz of chocolate cream.

On each sale, the cafe takes a profit of 5100 won(Korean won) per cup of Cafe Mocha,
4600 won per cup of Caffe Latte and 5300 won of chocolate milk.

The owner of cafe wishes to maximize its profit.
How many cup of beverage shold it produce respectively?
'''

'''
Vector c is coefficients of a linear objective function.
Matrix A is coefficients of constraints inequalities.
Vector b is constants of constraints.
'''
c = np.array([5100, 4600, 5300])
A = np.array([[  2,    2,   0],
              [  4,  4.5,   5],
              [  1,    0, 2.5]])
b = np.array([120, 300, 80])

var, opt = gsimplex.maxlinprog(c, A, b)
print('variables(Cafe Mocha, Caffe Latte, Chocolate milk) =', var)
print('optimal value(Profit) =', opt)

