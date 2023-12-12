import numpy as np
A = np.array([[2, 3, -1],
              [1, 2, 1],
              [3, 1, -2]])
b = np.array([7, 3, 8])
print("SJC22MCA2027- Georgekutty Biju\nS3MCA")
try:
    X = np.linalg.solve(A, b)
    print("Solution X:")
    print(X)
except np.linalg.LinAlgError:
    print("Matrix A is singular. The system of equations may not have a unique solution.")