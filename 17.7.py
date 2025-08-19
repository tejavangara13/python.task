#conditional statement
#if

# age=19

# if age >= 18:
#     print('I can vote')
#     print('Dabbulu vastayi')
# if age <=18:    
#  print('Iconnt vote')
#  print('Dabbulu vastayi')    

# num=int(input('enter number'))

# if num >1:
#    print('the number is positive')
# num = int(input("Enter number: "))
# if num % 2 == 0:
#    print("The number is even")
# else:
#    print("The number is odd")  


# for num in range(1,101):

#  if num % 7 == 0:
#     print(num)

# str1 =('Teja1301')

# if len(str1) > 10:
#     print("password is strong")
# else:
#     print("password is week")


# num = 0
# if num > 0:
#     print("positive number")
# else:
#     if num == 0:
#         print("Zero")
#     else:    
#       print("negitive number")    


# num = float(input("Enter a number: "))

# if num > 0:
#     print("The number is positive.")
# elif num < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# num = int(input("Enter an integer: "))
  
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}.")
# else:
#     print("Both numbers are equal.")

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Eligible to vote.")
# else:
#     print("Not eligible to vote.")

# marks = float(input("Enter your marks (0–100): "))

# if 0 <= marks <= 100:
    
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 60:
#         print("Grade C")
#     elif marks >= 40:
#         print("Grade D")
#     else:
#         print("Fail")
# else:
#     print("Invalid marks. Please enter a value between 0 and 100.")

# num = float(input("Enter a number: "))

# if num > 0:
#     print("Positive number")
#     if num % 2 == 0:
#         print("It is even.")
#     else:
#         print("It is odd.")
# elif num < 0:
#     print("Negative number")
# else:
#     print("Zero")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator. Please enter one of +, -, *, /.")
