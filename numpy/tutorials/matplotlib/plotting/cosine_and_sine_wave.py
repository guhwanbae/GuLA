import numpy as np
import matplotlib.pyplot as plt

# Set the x coordinate resolution.
n = 100
length = 4 * np.pi
step = length / n

# Compute cosine and sine wave points.
x = np.arange(0, length, step)
y_cos = np.cos(x)
y_sin = np.sin(x)

# Plot cosine and sine wave points using matplotlib.
plt.plot(x, y_cos)
plt.plot(x, y_sin)
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Cosine and Sine wave")
plt.legend(['Cosine', 'Sine'])
plt.show()
