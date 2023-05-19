# Recursive Least Squares (RLS) method:
import numpy as np

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# RLS parameters
n = 2  # System order
lambda_val = 0.98  # Forgetting factor

# Initialize the numerator and denominator coefficients
numerator = np.zeros(n+1)
denominator = np.zeros(n+1)
denominator[-1] = 1

# Initialize the state vectors and matrices
P = np.eye(n+1)
x = np.zeros(n+1)

# Recursive Least Squares algorithm
for k in range(len(output_data)):
    # Construct the regressor vector
    regressor = np.concatenate(([1], -output_data[k-n:k][::-1]))

    # Calculate the predicted output
    y_pred = np.dot(regressor, numerator)

    # Calculate the prediction error
    prediction_error = output_data[k] - y_pred

    # Update the gain matrix
    k_gain = np.dot(P, regressor) / (lambda_val + np.dot(regressor, np.dot(P, regressor)))

    # Update the numerator and denominator coefficients
    numerator += k_gain * prediction_error
    denominator -= np.dot(k_gain, regressor)

    # Update the state vectors and matrices
    P = (P - np.outer(k_gain, np.dot(regressor, P))) / lambda_val
    x = np.dot(regressor, numerator)

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
