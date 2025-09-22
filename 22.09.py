
# 1. "Given a list where each element represents the color of a sock, e.g., ['red', 'green', 'red', 'purple', 'green', 'black', 'red'], how many days can I sustain if I can wear only one matching pair of socks per day and each pair can be used only once?"

# 2. Find the missing numbers. Input: 34571  	Output : 26 missing

# 3. Matrix addition using range.

socks = ['red', 'green', 'red', 'purple', 'green', 'black', 'red']

from collections import Counter

def sock_days(socks):
    counts = Counter(socks)         # count occurrences of each color
    pairs = sum(v // 2 for v in counts.values())  # count pairs per color
    return pairs

socks = ['red', 'green', 'red', 'purple', 'green', 'black', 'red']
print("Days sustained:", sock_days(socks))


#
def missing_digits(num):
    digits = set(str(num))
    all_digits = set("0123456789")
    missing = all_digits - digits
    return "".join(sorted(missing)), len(missing)

num = 34571
missing, count = missing_digits(num)
print("Missing digits:", missing)
print("Count:", count)



#
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [1, 2, 3]]

rows, cols = len(A), len(A[0])

result = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        result[i][j] = A[i][j] + B[i][j]

print("Matrix Addition Result:")
for row in result:
    print(row)

