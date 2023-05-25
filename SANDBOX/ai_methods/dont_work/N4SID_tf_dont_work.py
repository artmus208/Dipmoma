#  Subspace Identification method a.k.a  N4SID method
import numpy as np
from scipy.linalg import svd, toeplitz
from scipy.signal import tf2ss, ss2tf

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# Define the system order and number of block rows
n = 2
p = 1

# Hankel matrix construction
L = input_data.shape[0] - 2 * p + 1
H = np.zeros((p * L, n * p))
for i in range(p * L):
    H[i] = np.hstack(input_data[i:i+p][::-1])

# Singular value decomposition (SVD)
U, S, Vh = svd(H)

# Determine the observability matrix O
O = U[:, :n] * np.sqrt(S[:n])

# Perform subspace identification
Y = output_data[p:L+p]
Y_shifted = output_data[:L].reshape(-1, 1)
theta = np.linalg.lstsq(O, Y - Y_shifted, rcond=None)[0]
A, B, C, D = np.zeros((n, n)), np.zeros((n, p)), np.zeros((p, n)), np.zeros((p, p))

A[:, :] = toeplitz(theta[:n], np.concatenate(([theta[0]], np.zeros(n-1))))
C[:, :] = toeplitz(theta[n:], np.concatenate(([theta[n-1]], np.zeros(p-1))))

# Convert state-space representation to transfer function representation
sys_ss = tf2ss(A, B, C, D)
num, den = ss2tf(sys_ss.A, sys_ss.B, sys_ss.C, sys_ss.D)

# Print the numerator and denominator coefficients
print("Numerator coefficients:", num)
print("Denominator coefficients:", den)
