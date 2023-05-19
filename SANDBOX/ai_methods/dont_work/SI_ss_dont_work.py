# Subspace Identification method for estimating the state-space representation of a system:
import numpy as np
from scipy.linalg import svd

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# System order
n = 2

# Construct the data matrix Y
Y = np.concatenate([output_data[i:i+n].reshape(1, -1) for i in range(len(output_data)-n+1)], axis=0)

# Perform singular value decomposition
U, _, _ = svd(Y, full_matrices=False)

# Estimate the observability matrix
Ob = U[:, :n]

# Estimate the system matrices A, B, C, and D
Y_shifted = np.concatenate([output_data[i:i+n].reshape(1, -1) for i in range(1, len(output_data)-n+1)], axis=0)
X = np.concatenate((Y_shifted.T, input_data[n:].T), axis=0)
X_ob = np.dot(Ob.T, X)
X_ob_pinv = np.linalg.pinv(X_ob)
X_ob_shifted = np.concatenate([X_ob[:, i:i+n].reshape(n, -1) for i in range(1, X_ob.shape[1]-n+1)], axis=1)
X_ob_shifted_pinv = np.linalg.pinv(X_ob_shifted)
X_ob_shifted_plus = np.dot(X_ob_shifted_pinv, X_ob_shifted)
X_ob_shifted_minus = np.dot(X_ob_shifted_pinv, X_ob[:, n:])
A_est = np.dot(X_ob_shifted_minus, X_ob_pinv)
C_est = np.dot(Ob, X_ob_pinv)
B_est = np.dot(A_est, X_ob[:, :n])
D_est = np.dot(C_est, input_data[:n].T)

# Print the estimated system matrices
print("Estimated A matrix:\n", A_est)
print("Estimated B matrix:\n", B_est)
print("Estimated C matrix:\n", C_est)
print("Estimated D matrix:\n", D_est)
