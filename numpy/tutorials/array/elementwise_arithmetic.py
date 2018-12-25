import numpy as np

x = np.array([[7, 6], [5, 4]], dtype=np.float64)
y = np.array([[3, 2], [1, 0]], dtype=np.float64)

print("Elementwise sum.")
print(x + y)
# It is same as below statement.
print(np.add(x, y))

print("Elementwise difference.")
print(x - y)
# It is same as below statement.
print(np.subtract(x, y))

print("Elementwise product.")
print(x * y)
# It is same as below statement.
print(np.multiply(x, y))

print("Elementwise division.")
print(x / y)
# It is same as below statement.
print(np.divide(x, y))
# Note this! Divide by zero occurs runtime warning.
# And the result value is 'inf'(Not a Number).

print("Elementwise square root.")
print(np.sqrt(x))
