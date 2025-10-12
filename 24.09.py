# 1. Check if the given matrix is an identity matrix
matrix = [[1,0,0],
          [0,1,0],
          [0,0,1]]

flag = True
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i == j and matrix[i][j] != 1) or (i != j and matrix[i][j] != 0):
            flag = False
            break

if flag:
    print("Identity matrix")
else:
    print("Not an identity matrix")


# 2. Add two matrices
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[9,8,7],
     [6,5,4],
     [3,2,1]]

sum_matrix = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    sum_matrix.append(row)

print("\nSum of two matrices:")
for r in sum_matrix:
    print(r)


# 3. Sum of diagonal elements
sum_diag = 0
for i in range(len(A)):
    sum_diag += A[i][i]
print("\nSum of diagonal elements:", sum_diag)


# 4. Matrix multiplication
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

print("\nMultiplication of two matrices:")
for r in result:
    print(r)