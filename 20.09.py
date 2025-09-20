# 1) Check duplicate digits in each number
def has_duplicate_digits(n):
    """Return True if integer n has any duplicate digits, otherwise False."""
    s = str(abs(int(n)))       # ignore sign and ensure integer
    return len(set(s)) < len(s)

def duplicates_for_list(nums, as_strings=False):
    """Return list of booleans for each number in nums indicating duplicate digits.
       If as_strings=True, returns 'true'/'false' strings (lowercase) like the example."""
    result = [has_duplicate_digits(x) for x in nums]
    if as_strings:
        return ['true' if r else 'false' for r in result]
    return result

# 2) Sum of all numbers in a matrix (list of lists)
def sum_matrix(matrix):
    """Return sum of all numeric entries in a 2D matrix (list of lists)."""
    # Safe approach: iterate rows and sum elements (works for irregular row lengths)
    total = 0
    for row in matrix:
        for val in row:
            total += val
    return total

# Example usage with the input you gave:
nums = [202, 89, 112, 88]
print("Input:", nums)
print("Duplicate digits (booleans):", duplicates_for_list(nums))
print("Duplicate digits (lowercase strings):", duplicates_for_list(nums, as_strings=True))
# Expected output: [True, False, True, True] and ['true','false','true','true']

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("Sum of all numbers in matrix:", sum_matrix(matrix))
# Expected output: 45
