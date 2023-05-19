# MAXIMUM LIKEHOOD ESTIMATION
import numpy as np
from scipy.optimize import minimize

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Transfer function order
n = 2

# Define the cost function for MLE estimation
def cost_function(coefficients):
    b = coefficients[:n+1]
    a = coefficients[n+1:]
    
    # Construct the transfer function
    num = np.poly1d(b)
    den = np.poly1d(np.concatenate(([1], a)))
    
    # Calculate the output of the transfer function
    y = np.zeros(output_data.shape[0])
    for i in range(n, output_data.shape[0]):
        y[i] = np.polyval(num, input_data[i]) / np.polyval(den, input_data[i])
    
    # Calculate the negative log-likelihood as the cost
    cost = -np.sum(np.log(y) + (output_data[n:] - y)**2 / 2)
    return cost

# Initial guess for coefficients
initial_coefficients = np.zeros(2 * (n+1))

# Perform Maximum Likelihood Estimation
result = minimize(cost_function, initial_coefficients, method='Nelder-Mead')

# Extract the estimated coefficients
estimated_coefficients = result.x
numerator = estimated_coefficients[:n+1]
denominator = estimated_coefficients[n+1:]

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
