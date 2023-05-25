# Recursive Least Squares (RLS) method for estimating the numerator and denominator coefficients of a transfer function:
import numpy as np

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Define the system order
n = 2

# Initialize the RLS algorithm parameters
lmbda = 0.98  # Forgetting factor
P = np.eye(n)  # Covariance matrix
theta = np.zeros(n)  # Parameter vector

# Perform Recursive Least Squares estimation
for i in range(output_data.shape[0] - n):
    u = input_data[i + n - 1]
    y = output_data[i + n]
    
    Phi = np.flip(input_data[i:i + n], axis=0)
    k = P @ Phi.T / (lmbda + Phi @ P @ Phi.T)
    e = y - Phi @ theta
    
    theta += k.flatten() * e
    P = (1 / lmbda) * (P - k @ Phi @ P)
    
# Extract numerator and denominator coefficients
numerator = theta
denominator = np.concatenate(([1], -theta))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
