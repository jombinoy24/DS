import numpy as np

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter the element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

# Input matrices from the user
print("Matrix 1:")
matrix1 = input_matrix()

print("\nMatrix 2:")
matrix2 = input_matrix()

# Perform matrix operations
addition_result = matrix1 + matrix2
print("\na. Addition Result:")
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
