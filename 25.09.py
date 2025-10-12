A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
I = [[1, 0], [0, 1]]

# 1. Check if the given matrix is an identity matrix
def is_identity(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j and matrix[i][j] != 1) or (i != j and matrix[i][j] != 0):
                return False
    return True
print("Is identity:", is_identity(I))

# 2. Add 2 matrixs
def add_matrices(a,b):
    result=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        result.append(row)
    return result
print("Matrix addition:", add_matrices(A, B))  


#   3. Sum of diagonal elements =>     
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total
print("Diagonal sum:", diagonal_sum(A))

# 4. Matrix multiplication
def multiply_matrices(a,b):
    result=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(b[0])):
            total=0
            for k in range(len(b)):
                total+= a[i][k]*b[k][j]
            row.append(total)
        result.append(row)
    return result
print("Matrix multipilication:",multiply_matrices(A,B))            


# 5. Transpose of a matrix
def transpose(matrix):
    result=[]
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix[0])):
            row.append(matrix[j][i])
        result.append(row)
    return result
print("Transpose:",transpose(A))


