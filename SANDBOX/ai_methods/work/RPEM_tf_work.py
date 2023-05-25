#  Recursive Prediction Error Method 
import numpy as np

# Input data (known inputs)
input_data = np.array([[1, 2],
                       [3, 4],
                       [5, 6],
                       [7, 8]])

# Output data (corresponding measurements)
output_data = np.array([10, 15, 20, 25])

# RPEM parameters
n = 2  # System order

# Initialize the numerator and denominator coefficients
numerator = np.zeros(n+1)
denominator = np.zeros(n+1)
denominator[-1] = 1

# Recursive prediction error method
for k in range(n, len(output_data)):
    # Construct the regressor vector
    regressor = np.concatenate(([1], -output_data[k-n:k][::-1]))

    # Predict the output
    y_pred = np.dot(regressor, numerator)

    # Calculate the prediction error
    prediction_error = output_data[k] - y_pred

    # Update the numerator and denominator coefficients
    numerator += 2 * prediction_error * regressor
    denominator += 2 * prediction_error * regressor

# Print the numerator and denominator coefficients
print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
