# # type of triangles
# # Check triangle inequality
# # Taking input from user
# # Call the function
# def Triangle_Checker(side1, side2, side3):
#     if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
#         if side1 == side2 == side3:
#             print('Equilateral Triangle')
#         elif side1 == side2 or side2 == side3 or side1 == side3:
#             print("Isosceles Triangle")
#         else:
#             print("Scalene Triangle")
#     else:
#         print("Invalid Triangle")
# side1 = float(input("Enter first side: "))
# side2 = float(input("Enter second side: "))
# side3 = float(input("Enter third side: "))

# Triangle_Checker(side1, side2, side3)

# for i in range(1,101):
#     print(i)

# n = int(input("Enter a number: "))
# sum_n = 0

# for i in range(1, n + 1):
#     sum_n += i

# print("Sum of first", n, "natural numbers is:", sum_n)

# def sum_of_natural_number(num):
#     sum=0
#     for i in range(1,num+1):
#       sum+=i
#     print(sum)
# sum_of_natural_number(10)
# sum_of_natural_number(20)

# i = 2  
# while i <= 50:
#     print(i)
#     i += 2  

# Input sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check if sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    print("\nThe sides form a triangle.")

    # Type of triangle
    if a == b == c:
        print("It is an Equilateral triangle.")
    elif a == b or b == c or a == c:
        print("It is an Isosceles triangle.")
    else:
        print("It is a Scalene triangle.")

    # Check for right-angled triangle
    sides = sorted([a, b, c])
    if round(sides[0]**2 + sides[1]**2, 5) == round(sides[2]**2, 5):
        print("It is also a Right-angled triangle.")
    else:
        print("It is not a Right-angled triangle.")
else:
    print("The given sides do NOT form a valid triangle.")




