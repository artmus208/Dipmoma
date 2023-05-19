# Nonlinear Least Squares method
import numpy as np
from scipy.optimize import least_squares

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Nonlinear transfer function model
def transfer_function(params, x):
    numerator = params[0] * x[0] + params[1] * x[1]
    denominator = 1 + params[2] * x[0] + params[3] * x[1]
    return numerator / denominator

# Residual function for the least squares optimization
def residual(params, x, y):
    return transfer_function(params, x) - y

# Initial guess for the parameters
initial_params = [1, 1, 0.5, 0.5]

# Perform the nonlinear least squares optimization
result = least_squares(residual, initial_params, args=(input_data.T, output_data))

# Extract the estimated parameters
estimated_params = result.x

# Print the estimated parameters
print("Estimated parameters:", estimated_params)
