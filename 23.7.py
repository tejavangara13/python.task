# num = int(input("Enter a number: "))

# print(f"Factors of {num} are:")

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

# num = 2

# while num <= 10:
#     print(num)
#     num += 2

# total = 0
# num = 1

# while num <= 5:
#     total += num
#     num += 1

# print("Sum of numbers from 1 to 5 is:", total)
# text = input("Enter a string: ")

# if text.isupper():
#     print("Upper case")
# else:
#     print("Lower case")
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch.isupper():
        print("Converted to lowercase:", ch.lower())
    elif ch.islower():
        print("It is already lowercase:", ch)
    else:
        print("Not an alphabetic letter:", ch)