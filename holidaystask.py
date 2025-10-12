# 1. Check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 2. Find the maximum and minimum element in a list
lst = [3, 1, 7, 0, 5]
max_val = lst[0]
min_val = lst[0]
for num in lst:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print("Max:", max_val)
print("Min:", min_val) 

# 3. Reverse a string without using slicing ([::-1])
s = input("Enter a string: ")
reversed_str = ''
for char in s:
    reversed_str = char + reversed_str
print("Reversed:", reversed_str)

# 4. Check if a string is a palindrome
s = input("Enter a string: ")
is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        is_palindrome = False
        break
print("Palindrome" if is_palindrome else "Not a palindrome")

# 5. Find the factorial of a number (using loop)
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)


# 6. Count the frequency of each character in a string
s = input("Enter a string: ")
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# 7. Find the second largest number in a list
lst = [5, 3, 9, 1, 9, 6]
first = second = float('-inf')
for num in lst:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print("Second largest:", second)


# 8. Count how many vowels and consonants are in a string
s = input("Enter a string: ").lower()
vowels = 'aeiou'
vowel_count = consonant_count = 0
for char in s:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 9. Calculate the sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits:", sum_digits)

# 10. Print the multiplication table of a number
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 11. Find the largest word in a given sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
largest_word = ""
for word in words:
    if len(word) > len(largest_word):
        largest_word = word
print("Largest word:", largest_word)

# 12. Remove all duplicate elements from a list
lst = [1, 2, 2, 3, 4, 4, 5]
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
print("Without duplicates:", unique)

# 13. Sort a list without using Python’s built-in .sort()
lst = [4, 2, 5, 1, 3]
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Sorted list:", lst)

# 14. Merge two lists into a single sorted list
a = [1, 3, 5]
b = [2, 4, 6]
merged = a + b
for i in range(len(merged)):
    for j in range(i + 1, len(merged)):
        if merged[i] > merged[j]:
            merged[i], merged[j] = merged[j], merged[i]
print("Merged and sorted:", merged)

# 15. Check if a number is a prime number
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not Prime")

#Medium questins python
# 1. Find all pairs in a list that sum up to a target value
lst = [2, 4, 3, 5, 7, 8, 9]
target = 10
pairs = []

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))

print("Pairs:", pairs)


# 2. Rotate a list by k positions
lst = [1, 2, 3, 4, 5]
k = 2  
k = k % len(lst)  
rotated = lst[-k:] + lst[:-k]
print("Rotated list:", rotated)

# 3. Find the missing number in a list of consecutive integers
lst = [1, 2, 3, 5, 6]
n = len(lst) + 1 
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
missing = expected_sum - actual_sum
print("Missing number:", missing)


# 4. Check if two strings are anagrams
str1 = "listen"
str2 = "silent"
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")


# 5. Count the number of words in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))


# 6. Remove all duplicate words from a sentence
sentence = "this is a test this is only a test"
words = sentence.split()
unique = []
for word in words:
    if word not in unique:
        unique.append(word)
print("Without duplicates:", ' '.join(unique))


# 7. Invert a dictionary (keys become values and vice versa)
d = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in d.items()}
print("Inverted dictionary:", inverted)


# 8. Find the intersection of two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection = [i for i in a if i in b]
print("Intersection:", intersection)


# 9. Print the transpose of a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)
print("Transpose:", transpose)


# 10. Implement bubble sort
lst = [5, 1, 4, 2, 8]
n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print("Sorted list:", lst)


# 11. Find the first non-repeating character in a string
s = "aabbcddex"
for char in s:
    if s.count(char) == 1:
        print("First non-repeating character:", char)
        break


# 12. Find the longest word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)


# 13. Find the second smallest number in a list
lst = [4, 1, 7, 3, 2]
first = second = float('inf')
for num in lst:
    if num < first:
        second = first
        first = num
    elif first < num < second:
        second = num
print("Second smallest:", second)


# 14. Check if a number is an Armstrong number

num = int(input("Enter a number: "))
num_str = str(num)
n = len(num_str)
total = sum(int(digit) ** n for digit in num_str)
if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")



