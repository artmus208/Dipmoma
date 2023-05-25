# Instrumental Variables Method
import numpy as np
from scipy.optimize import minimize

def toeplitz_matrices(input_signal, order):
    input_signal_padded = np.concatenate(([0] * order, input_signal))
    input_matrix = np.column_stack([input_signal_padded[i:i + len(input_signal)] for i in range(order + 1)])
    return input_matrix[:-order]

def transfer_function(coef, input_signal):
    num = coef[:len(coef)//2]
    den = coef[len(coef)//2:]
    return np.convolve(num, input_signal, mode='full')[:len(input_signal)] / np.convolve(den, input_signal, mode='full')[:len(input_signal)]

def iv_error_function(coef, input_signal, output_signal, order):
    input_matrix = toeplitz_matrices(input_signal, order)
    num = coef[:order+1]
    den = coef[order+1:]
    y = np.convolve(den, input_signal, mode='full')[:len(input_signal)]
    x = input_matrix @ num
    x = x[:len(input_signal)]
    output_signal = output_signal[:len(input_signal)]  # Обрезаем длину вектора output_signal
    y = y[:len(input_signal)]  # Обрезаем длину вектора y
    return np.sum((output_signal - y - x) ** 2)

# Пример использования
input_signal = np.array([1, 2, 3, 4, 5])
true_num = np.array([2, 3])
true_den = np.array([1, -0.5])
true_output = transfer_function(np.concatenate((true_num, true_den)), input_signal)

order = 2  # Порядок модели (степень многочлена в числителе и знаменателе)
initial_coef = np.ones(order * 2 + 2)  # Начальные значения коэффициентов передаточной функции
result = minimize(iv_error_function, initial_coef, args=(input_signal, true_output, order), method='Nelder-Mead')
estimated_coef = result.x
print("Estimated numerator coefficients:", estimated_coef[:order+1])
print("Estimated denominator coefficients:", estimated_coef[order+1:])

