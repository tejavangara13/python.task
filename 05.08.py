# negative,positive and zero check the numbers
# def check_num_status(num):
#     if num>0:
#         print('positive')
#     else:
#         if num==0:
#             print('zero')
#         else:
#             print('negative')
# num_input=int(input('enter a number:'))
# check_num_status(num_input) 

# or

# def check_num_status(num):
#     if num>0:
#         return 'positive'
#     elif num==0:
#         return 'zero'
#     else:
#         return 'negative'
# n1=check_num_status(8)
# print(n1)

# # ever or add check
# def check_even_or_odd(num1):
#     res='even'if num1%2==0 else 'odd'
#     print(res)
# check_even_or_odd(9)

# # the gretest of two numbers with using terminal

# def check_gretest(num1,num2):
#     return num1 if num1>num2 else num2
# print(check_gretest(-5,2))

# # without using terminal

# def check_gretest(num1,num2):
#     if num1>num2:
#         return num1
#     elif num1==num2:
#         return 'both are equal'
#     else:
#         return num1
# print(check_gretest(-2,4)) 

# num=int(input('enter a no:'))
# if num==1:
#     print('mondY')
# elif num==2:
#     print('tue')
# elif num==3:
#     print('wed')
# elif num==4:
#     print('thursday')
# elif num==5:
#     print('friday')
# elif num==6:
#     print('saturday') 


# num=int(input('Enter a month no:'))
# if num==1:
#     print('january')
# elif num==2:
#     print('february') 
# elif num==3:
#     print('march')
# elif num==4:
#     print('april')
# elif num==5:
#     print('may')
# elif num==6:
#     print('june')
# elif num==7:
#     print('july')
# else:
#     print('enter a month no:') 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b and a > c:
#     print("Greatest number is:", a)
# elif b > c:
#     print("Greatest number is:", b)
# else:
#     print("Greatest number is:", c)   

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0):
#     print(year, "is a leap year.")
# else:
#     print(year, "is not a leap year.")  

# ch = input("Enter a single character: ")

# if len(ch) != 1 or not ch.isalpha():
#     print("Not a valid alphabet character.")
# elif ch.lower() in 'aeiou':
#     print(ch, "is a vowel.")
# else:
#     print(ch, "is a consonant.") 

def Grade_Calculator(marks):
  print('Grade: A' if marks >= 90 else 
           'Grade: B' if marks >= 80 else 
           'Grade: C' if marks >= 70 else 
           'Fail')

marks = int(input("Enter marks: "))
Grade_Calculator(marks)  
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Valid triangle")
else:
    print("Not a valid triangle")                          
    

    


