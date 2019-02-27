# Author    :   Gu-hwan Bae
# Summary   :   Find a local minima by using gradient descent.

import numpy as np
import matplotlib.pyplot as plt

def gradientDescent(init, df, step, precision, max_iters):
    cur = init
    diff = 1
    iters = 0
    trace = []
    while diff > precision and iters < max_iters:
        trace += [cur]
        prev = cur
        cur -= step * df(prev)
        diff = abs(cur - prev)
        iters += 1
    return cur, trace

f = lambda x: 0.01*x**5 - 3*x**3
df = lambda x: 0.05*x**4 - 9*x**2
init_x = 20
step = 1e-5
precision = 1e-9
max_iters = 10000

lm, trace = gradientDescent(init_x, df, step, precision, max_iters)

trace = np.asarray(trace)

x = np.linspace(-20, 20, 100)

plt.plot(x, f(x))
plt.plot(trace, f(trace))
plt.show()

print('Local minimum = lm =', lm)
print('f(lm) =', f(lm))
print('df(lm) =', df(lm))

