#for loop converted to while loop
# class_no=1
# while class_no<11:
#     roll_no=1
#     while roll_no<31:
#         print('class',class_no,'roll',roll_no)
#         roll_no+=1
#     class_no+=1 

#jump statements-continue,break and pass
# continue and break only using loop
# break
# for i in range(1,20):
#     print(i)
#     if i==5:
#        break 
#     print(i) 


# for i in range(1,20):
#     if i <5:
#         print(i)
#         print(i)
#     elif i == 5:
#         print(i)
         
# for i in range(1,31):
#     print(i*2567)
#     break 
#     print(i*2567) 

# for i in range(1,31):
#     if i < i* (-1):
#         break
#     print(i**2)

# for i in range(1,31):
   
#      print(i**2) 

# for i in range(0,31):
#      if i <i * (-1) or i % 5 == 0:
#           break
#      print(i**2)

#continue
# for i in range(1,34):
#     print(i)
#     print(i)
#     if i == 6:
#         continue
#     print(i)


# for i in range(1,45):
#     continue
#     print(i) 

# i = 5
# while i < 25:
#     print(i)
#     i -=1


# i = 5
# while i < 25:
#     print(i)
#     i -=1
#     if i % 5 == 0:
#         break


#break and continue in nested loop
# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         if roll_no ==5:
#             break
#         print('class',class_no,'roll',roll_no)  
# # 
# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         if roll_no ==5:
#             continue
#         print('class',class_no,'roll',roll_no)      
    
#pass

# num1 = 10

# if num1 % 2 == 0:
#     pass
# else:
#     print('Number is odd')



# def sum():
#     pass 
# 
# for class_no in range(1,11):
#     for roll_no in range(1,31):
#         if class_no %  5==0 or roll_no < 15:
#              break
#         print('class',class_no,'roll',roll_no)   

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}.")
# else:
#     print("Both numbers are equal.")

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# if num1 >= num2 and num1 >= num3:
#     print(f"The greatest number is {num1}.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"The greatest number is {num2}.")
# else:
#     print(f"The greatest number is {num3}.")

# number = float(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")

# n = int(input("Enter a positive integer: "))

# total = 0

# for i in range(1, n + 1):
#     total += i
# print(f"The sum of the first {n} natural numbers is {total}.")

# n = int(input("Enter a number: "))

# print(f"Even numbers from 1 to {n} are:")
# for i in range(2, n + 1, 2):
#     print(i)

# num = int(input("Enter a number to print its multiplication table: "))

# print(f"\nMultiplication table of {num}:")
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

# i = 1

# while i <= 10:
#     print(i)
#     i += 1



# num = int(input("Enter a number: "))

# digit_sum = 0

# while num > 0:
#     digit = num % 10       
#     digit_sum += digit     
#     num = num // 10        

# print(f"The sum of the digits is {digit_sum}.")


# correct_password = "mypassword"  

# attempts = 3

# while attempts > 0:
#     entered_password = input("Enter your password: ")
    
#     if entered_password == correct_password:
#         print("Login successful!")
#         break
#     else:
#         attempts -= 1
#         print(f"Incorrect password. Attempts left: {attempts}")

# if attempts == 0:
#     print("Account locked.")

# for i in range(1, 21):
#     if i % 3 == 0:
#         continue  
#     print(i)

# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         print("Zero entered, stopping the program.")
#         break
#     else:
#         print(f"You entered: {num}")


# even_count = 0
# odd_count = 0

# print("Enter 5 numbers:")

# for i in range(5):
#     num = int(input(f"Number {i + 1}: "))
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print(f"\nEven numbers: {even_count}")
# print(f"Odd numbers: {odd_count}")

# word = input("Enter a word: ")

# print("\nCharacters in the word:")
# for char in word:
#     print(char)

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 2 and 5.")
else:
    print(f"{num} is NOT divisible by both 2 and 5.")