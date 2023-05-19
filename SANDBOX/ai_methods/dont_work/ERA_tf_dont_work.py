# Eigensystem Realization Algorithm
import numpy as np
from scipy.linalg import solve
from scipy.linalg import eig

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# System order
n = 2

# Construct the Hankel matrices H0 and H1
H0 = np.concatenate([output_data[i:i + n].reshape(1, -1) for i in range(len(output_data) - n)], axis=0)
H1 = np.concatenate([input_data[i:i + n].reshape(1, -1) for i in range(len(input_data) - n)], axis=0)

# Perform eigendecomposition
Q, S, Qh = eig(H0.T @ H0, H0.T @ H1)
idx = np.argsort(np.abs(S))[::-1]
Q = Q[:, idx]
S = S[idx]
Qh = Qh[:, idx]

# Estimate the system matrices A and C
A_est = Qh[:n, :] @ np.diag(np.sqrt(S[:n]))
C_est = solve(np.conj(A_est.T), H0.T @ output_data[n:])

# Extract numerator and denominator coefficients
numerator = C_est
denominator = np.concatenate(([1], -A_est[0]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
