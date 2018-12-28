import numpy as np
import matplotlib.pyplot as plt

# Set the x coordinate resolution.
n = 100
length = 3 * np.pi
step = length/n

# Compute the x and y coordinates for points.
x = np.arange(0, length, step)
y = np.sin(x)

# Plot the points using matplotlib.
print("Number of points : %d, step : %f" % (n, step))
plt.plot(x, y)
plt.show()
