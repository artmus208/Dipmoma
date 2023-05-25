# Stochastic Subspace Identification

import numpy as np
from scipy.linalg import svd
from scipy.linalg import solve

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# System order
n = 2
m = input_data.shape[1]  # Number of inputs

# Construct the data matrix Y
Y = np.concatenate([output_data[i:i+n].reshape(1, -1) for i in range(len(output_data)-n+1)], axis=0)

# Perform singular value decomposition
U, _, _ = svd(Y, full_matrices=False)

# Estimate the system matrices A and C
U1 = U[:-n, :n]
U2 = U[:-n, n:]
U2_perp = U2[:, np.argsort(np.linalg.norm(U2, axis=0))]
U1_perp = U1[:, np.argsort(np.linalg.norm(U2, axis=0))]
Y_perp = Y[:, np.argsort(np.linalg.norm(U2, axis=0))]
R = np.concatenate((U2_perp, Y_perp), axis=1)
A_est = solve(U1_perp, U2_perp.T @ U2_perp)
C_est = R @ np.linalg.pinv(U2_perp.T @ U2_perp) @ U2_perp.T @ Y_perp

# Extract numerator and denominator coefficients
numerator = C_est[0]
denominator = np.concatenate(([1], -A_est[0]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
