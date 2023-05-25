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

# Construct the regressor matrix Phi
m = input_data.shape[1]
l = output_data.shape[0] - n
Phi = np.zeros((l, n * m))
for i in range(l):
    for j in range(n):
        Phi[i, j * m:(j + 1) * m] = input_data[i + n - j - 1]

# Perform least squares estimation
coefficients = np.linalg.lstsq(Phi, output_data[n:], rcond=None)[0]

# Extract numerator and denominator coefficients
numerator = coefficients[:m]
denominator = np.concatenate(([1], -coefficients[m:]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
