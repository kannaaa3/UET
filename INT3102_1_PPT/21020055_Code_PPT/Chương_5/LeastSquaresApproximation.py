import numpy as np

# Given data points
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Degree of the polynomial
degree = 2

# Create the Vandermonde matrix
V = np.vander(x, degree + 1, increasing=True)

# Solve the least squares problem
coefficients, residuals, rank, singular_values = np.linalg.lstsq(V, y, rcond=None)

# Print the coefficients
print("Coefficients:", coefficients)
