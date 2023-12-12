import numpy as np;
def get_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)
# Get input matrices from the user
rows_X = int(input("Enter the number of rows for matrix X: "))
cols_X = int(input("Enter the number of columns for matrix X: "))
if rows_X != 2 or cols_X != 2:
    print("Please enter a 2x2 matrix.")
else:
    X = get_matrix_input(rows_X, cols_X)
    rows_Y = int(input("Enter the number of rows for matrix Y: "))
    cols_Y = int(input("Enter the number of columns for matrix Y: "))
    if rows_Y != 2 or cols_Y != 2:
        print("Please enter a 2x2 matrix.")
    else:
        Y = get_matrix_input(rows_Y, cols_Y)
print("Matrix X is : ",X)
print("Matrix Y is : ",Y)
a=np.power(X,2)
print("X^2=",a)
result = a + 2 * Y
print("X^2+2*Y = ",result)