# Least Absolute Deviations Method
from scipy.optimize import minimize
import numpy as np

def transfer_function(coef, input_signal):
    num = coef[:len(coef)//2]
    den = coef[len(coef)//2:]
    return np.convolve(num, input_signal, mode='full')[:len(input_signal)] / np.convolve(den, input_signal, mode='full')[:len(input_signal)]

def error_function(coef, input_signal, output_signal):
    num = coef[:len(coef)//2]
    den = coef[len(coef)//2:]
    model_output = np.convolve(num, input_signal, mode='full')[:len(input_signal)] / np.convolve(den, input_signal, mode='full')[:len(input_signal)]
    return np.sum(np.abs(model_output - output_signal))

# Пример использования
input_signal = np.array([1, 2, 3, 4, 5])
true_num = np.array([2, 3])
true_den = np.array([1, -0.5])
true_output = transfer_function(np.concatenate((true_num, true_den)), input_signal)

initial_coef = np.ones(4)  # Начальные значения коэффициентов передаточной функции
result = minimize(error_function, initial_coef, args=(input_signal, true_output), method='Nelder-Mead')
estimated_coef = result.x
print("Estimated numerator coefficients:", estimated_coef[:len(estimated_coef)//2])
print("Estimated denominator coefficients:", estimated_coef[len(estimated_coef)//2:])
