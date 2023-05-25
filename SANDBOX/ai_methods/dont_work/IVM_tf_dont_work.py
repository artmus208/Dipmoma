#  instrumental variable method
import numpy as np
from scipy.linalg import toeplitz, lstsq

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Transfer function order
n = 2

# Construct the regressor matrix X
X = np.zeros((output_data.shape[0] - n, n + 1))
for i in range(n, output_data.shape[0]):
    X[i - n] = np.flip(output_data[i-n:i+1])

# Construct the instrumental variable matrix Z
Z = np.zeros((input_data.shape[0] - n, n + 1))
for i in range(n, input_data.shape[0]):
    Z[i - n] = np.flip(input_data[i-n:i+1])

# Perform instrumental variable estimation
coefficients, _, _, _ = lstsq(Z, X, rcond=None)

# Extract numerator and denominator coefficients
numerator = coefficients[:, 0]
denominator = np.concatenate(([1], -coefficients[:, 1:]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
