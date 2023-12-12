import numpy as np

# Get matrix dimensions from the user
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))

# Initialize an empty matrix
A = np.empty((rows, cols))

# Get matrix elements from the user
for i in range(rows):
    for j in range(cols):
        A[i, j] = float(input(f"Enter element A[{i+1}, {j+1}]: "))

# Perform SVD
U, S, Vt = np.linalg.svd(A)
A_hat = U @ np.diag(S) @ Vt

# Display results
print("\nOriginal Matrix A:")
print(A)
print("\nSingular Values:")
print(S)
print("\nReconstructed Matrix A_hat:")
print(A_hat)
