import numpy as np
import matplotlib.pyplot as plt

# Set the x coordinate resolution.
n = 100
length = 10
step = length / n

# Compute the x and y coordinate logarithm points.
x = np.arange(0, length, step)
y_log = np.log(x)
y_reflect = y_log * -1

# The first plot is logarithm.
plt.subplot(2, 1, 1)
plt.plot(x, y_log)
plt.title("Log")

# The second plot is the reflected curve.
plt.subplot(2, 1, 2)
plt.plot(x, y_reflect)
plt.title("Reflected")

plt.show()
