# Keyword argument
# default arguments
def sum_num(a,b):
    print(a+b)
def sum_sum(a,b,c):    
    print(a+b+c)
def sum_bum(a,b,c,d):
    print(a+b+c+d) 

# sum(2,3)
# sum(4,5,6)
# sum(5,7,8,9)       

# def sum (a,*b):
#     print(a)
#     print(b)
    
# sum (2,3)
# sum (2,3,4,5)
# sum (2)
# sum (2,4,9,10,11,12)    

def print_sum(a, b):
    total = a + b
    print("The sum is:", total)
print_sum(3, 5)  

def print_square(number):
    square = number ** 2
    print("The square is:", square)
print_square(4)    

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
check_even_odd(7)  
check_even_odd(8)      


def print_factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"The factorial of {n} is: {factorial}")
print_factorial(5) 

def print_max_of_three(a, b, c):
    maximum = max(a, b, c)
    print(f"The maximum of the three numbers is: {maximum}")
print_max_of_three(10,25,17)       

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print(f"Number of vowels in the string: {count}")
count_vowels("Vangara Gnana Tejaswi")    
    
def print_list_sum(numbers):
    total = sum(numbers)
    print(f"The sum of the list elements is: {total}")
print_list_sum([1,2,3,4,5])    

def print_reversed_string(s):
    reversed_str = s[::-1]
    print(f"Reversed string: {reversed_str}")
print_reversed_string("TEJA") 

def check_palindrome(s):
    cleaned = s.lower().replace(" ", "")  
    if cleaned == cleaned[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')
check_palindrome("Madam")
check_palindrome("Hello World")  


def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Even numbers in the list:", even_numbers)
print_even_numbers([1,2,3,4,5,6,7,8,10])    

import math

def print_circle_area(radius):
    if radius < 0:
        print("Radius cannot be negative.")
        return
    area = math.pi * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area:.2f}")
print_circle_area(8)

def print_string_length(s):
    count = 0
    for _ in s:
        count += 1
    print(f"The length of the string is: {count}")
print_string_length("Vangara Gnana Tejaswi")    

def print_average(*args):
    if len(args) == 0:
        print("No numbers provided.")
        return
    total = sum(args)
    average = total / len(args)
    print(f"The average is: {average}")
print_average(4, 8, 15, 16, 23, 42)    