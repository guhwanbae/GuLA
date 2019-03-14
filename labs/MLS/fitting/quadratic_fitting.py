# Author  : Gu-hwan Bae
# Summary : Estimate the number of Korean CSAT applicants by using
#           the quadratic fitting.

import gula.qr as gQr
import numpy as np
import matplotlib.pyplot as plt

order = 2
# The applicants vector is the number of Korean CSAT applicants.
# The year vector is the year.
applicants = np.array([781749, 840661, 824374, 885321, 868643, 896122, 872297, 739129, 675922])
year = np.array([1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003])

# A is the matrix which contains coefficients of the quadratic polynomial.
A = np.full((applicants.shape[0],order+1), 1)
A[:,1] *= year
A[:,2] *= np.power(year, 2)

# u is the coefficient vector.
u = gQr.solve(A, applicants)

(c, b, a) = u
func = lambda x: a*(x**2) + b*x + c

n = 100
x = np.linspace(1993, 2005, n)
estimated = func(x)

plt.figure('Fitting')
plt.title('Quadratic fitting')
plt.scatter(year, applicants, color='r', marker='*', label='Given data')
plt.plot(x, estimated, color='c', label='Estimated(Quadratic fitting)')
plt.xlabel('year')
plt.ylabel('The number of Korean CSAT applicants')
plt.legend()
plt.grid()
plt.show()
