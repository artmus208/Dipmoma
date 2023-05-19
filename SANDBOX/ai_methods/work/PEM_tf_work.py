#  Prediction Error Method 

import numpy as np
from scipy.linalg import toeplitz
from scipy.linalg import pinv

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Transfer function order
n = 2

# Construct the regressor matrix Phi
Phi = np.zeros((output_data.shape[0] - n, n + 1))
for i in range(n, output_data.shape[0]):
    Phi[i - n] = np.flip(output_data[i-n:i+1])

# Perform the Prediction Error Method (PEM)
Phi_T = Phi.T
Theta = Phi_T @ Phi
Y = Phi_T @ output_data[n:]
G = pinv(Theta) @ Y

# Extract numerator and denominator coefficients
numerator = G[1:]
denominator = np.concatenate(([1], -G[:n]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
