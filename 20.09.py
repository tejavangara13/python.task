# Today's assignment:

# Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
# Input: [202,89,112,88]       	Output:[true ,false ,true ,true]

# Sum of all numbers in a matrix.
def has_duplicate_digits(num):
    digits = str(num)               
    for i in range(len(digits)):     
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:  
                return True
    return False  


numbers = [202, 89, 112, 88]
result = []
for num in numbers:
    result.append(has_duplicate_digits(num))

print("Output:", result)  



def sum_matrix(matrix):
    total = 0
    for i in range(len(matrix)):        
        for j in range(len(matrix[i])): 
            total += matrix[i][j]
    return total



matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix:", matrix)
print("Sum of all numbers:", sum_matrix(matrix))  



