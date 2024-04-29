def matrix_subtraction(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def matrix_input():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    print("Enter the elements row-wise separated by space:")
    for _ in range(rows):
        row = [float(x) for x in input().split()]
        matrix.append(row)
    return matrix

# Input matrices
print("Enter elements for matrix 1:")
matrix1 = matrix_input()

print("Enter elements for matrix 2:")
matrix2 = matrix_input()

# Add matrices
result_matrix = matrix_subtraction(matrix1, matrix2)

# Display result
print("\nResultant Matrix:")
for row in result_matrix:
    print(row)