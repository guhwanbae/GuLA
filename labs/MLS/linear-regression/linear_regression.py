# Author    :   Gu-hwan Bae
# Summary   :   Estimation with a linear regression.

import gula.qr as gQR
import numpy as np
import matplotlib.pyplot as plt

'''
The linear function, f(x) = a + cx, is represented
with a coefficient matrix, A.

fA(x) : A * x = c

The solution, x_est, solved by QR factorization is most approximate.
'''
A = np.array([[1, 1, 1, 1, 1],
              [45, 55, 65, 75, 85]]).T
b = np.array([4, 3.8, 3.75, 3.5, 3.3])

x_est = gQR.solve(A, b)
y_est = np.dot(A, x_est)
print(x_est)
print(y_est)

plt.figure('Estimation with linear regression')
plt.title('Estimation with linear regression')
plt.scatter(A[:,1], b, color='r', marker='*', label='Given data')
plt.plot(A[:,1], y_est, label='Estimated')
plt.xlabel('Age')
plt.ylabel('Drinking capacity')
plt.legend()
plt.show()
