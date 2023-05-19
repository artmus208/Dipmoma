# Subspace Identification method

import numpy as np
from scipy.linalg import block_diag
from scipy.linalg import svd
from scipy.linalg import pinv

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Subspace Identification parameters
n = 2  # System order
p = 2  # Number of block rows
m = input_data.shape[1]  # Number of inputs
l = output_data.shape[0]  # Number of data points

# Construct the Hankel matrices H0 and H1
H0 = block_diag(*[input_data[i:i + p] for i in range(n)]).T
H1 = block_diag(*[output_data[i:i + p] for i in range(n)]).T

# Perform singular value decomposition
U, s, Vh = svd(H0, full_matrices=False)

# Estimate the system matrices A and C
U1 = U[:, :n]
U2 = U[:, n:]
U2_perp = U2[:, np.argsort(-s[n:])]
Y = H1 @ Vh.T.conj()
Y2_perp = Y[:, np.argsort(-s[n:])]
Theta = np.concatenate((U2_perp, Y2_perp), axis=1)
Theta_dagger = pinv(Theta)
A_est = Theta_dagger[:n, :n]
C_est = Theta_dagger[n:, :n]

# Extract numerator and denominator coefficients
numerator = C_est[0]
denominator = np.concatenate(([1], -A_est[0]))

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
