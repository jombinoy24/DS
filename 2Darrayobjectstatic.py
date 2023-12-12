import numpy as np
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
addition_result = matrix1 + matrix2
print("a. Addition Result:")
print(addition_result)
subtraction_result = matrix1 - matrix2
print("\nb. Subtraction Result:")
print(subtraction_result)
multiplication_result = matrix1 * matrix2
print("\nc. Multiplication Result:")
print(multiplication_result)
epsilon = 1e-15
division_result = np.divide(matrix1, matrix2 + epsilon)
print("\nd. Division Result:")
print(division_result)
matrix_multiplication_result = np.dot(matrix1, matrix2)
print("\ne. Matrix Multiplication Result:")
print(matrix_multiplication_result)
transpose_result = np.transpose(matrix1)
print("\nf. Transpose of the Matrix:")
print(transpose_result)
diagonal_sum = np.trace(matrix1)
print("\ng. Sum of Diagonal Elements:")
print(diagonal_sum)

