# AutoRegressive with eXogenous inputs
import numpy as np

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# ARX model order
na = 2  # AR order
nb = 2  # X order

# Construct the regressor matrix Phi
l = output_data.shape[0] - na
Phi = np.zeros((l, na + nb * input_data.shape[1]))
for i in range(l):
    Phi[i, :na] = -output_data[i + na - 1:i - 1:-1]
    Phi[i, na:] = np.concatenate(input_data[i + na - 1:i - 1:-1])

# Perform least squares estimation
coefficients = np.linalg.lstsq(Phi, output_data[na:], rcond=None)[0]

# Extract numerator and denominator coefficients
numerator = np.concatenate(([0], coefficients[na:na + nb * input_data.shape[1]]))
denominator = np.concatenate(([1], coefficients[:na]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
