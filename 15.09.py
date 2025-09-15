# String reverse
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev   
    return rev
print("Reverse of 'Python' →", reverse_string("Python"))


# Sum of digits of each number in a given list
def sum_of_digits_list(numbers):
    result = []
    for num in numbers:
        total = 0
        for digit in str(abs(num)):  
            total += int(digit)
        result.append(total)
    return result
numbers = [123, 405, 89, 560]
print("Sum of digits for list →", sum_of_digits_list(numbers))

# Find max digit in the given number
def max_digit(num):
    maximum = 0
    for digit in str(abs(num)):
        d = int(digit)
        if d > maximum:
            maximum = d
    return maximum
num = 5834
print("Max digit in", num, "→", max_digit(num))

# Find max digit for every number in the given list
def max_digit_list(numbers):
    result = []
    for num in numbers:
        result.append(max_digit(num))
    return result

print("Max digit for each number in list →", max_digit_list(numbers))