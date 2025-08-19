# num1=10
# def check_function():
#     num1=20
#     globals()['num1']=30
#     print(num1)
# check_function()
# print(num1)


# num1=10
# def check_function():
#     num1=20
#     print(num1)
# check_function()
# print(num1)

# start = int(input("Enter start: "))
# end = int(input("Enter end: "))

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
start = int(input("Enter start: "))
end = int(input("Enter end: "))

prime = [True] * (end + 1)
prime[0] = prime[1] = False 

for i in range(2, int(end**0.5) + 1):
    if prime[i]:
        for j in range(i*i, end + 1, i):
            prime[j] = False

for num in range(start, end + 1):
    if prime[num]:
        print(num)



