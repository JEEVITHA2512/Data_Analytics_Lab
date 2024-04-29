def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

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

# Multiply matrices
result_matrix = matrix_multiplication(matrix1, matrix2)

# Display result
print("\nResultant Matrix:")
for row in result_matrix:
    print(row)



