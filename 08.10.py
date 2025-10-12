# def square_hollow_pattern(n):
#     for i in range(n):
#         for j in range(n):
#             if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()

# square_hollow_pattern(5)

# n = 4
# for i in range(1, n+1):
#     print((str(i) + " ") * i)


# n = 4
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# n = 4
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# n = 4
# num = 1
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(num, end=" ")
#         num += 1
#     print()

# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print((i+j+1) % 2, end=" ")
#     print()


# n = 4
# for i in range(1, n+1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     for j in range(2, i+1):
#         print(j, end="")
#     print()


# n = 5
# for i in range(n):
#     print(" " * (n-i-1) + "* " * n)


# n = 4
# for i in range(1, n+1):
#     print(" "*(n-i) + "* " * i)
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "* " * i)


# n = 4
# for i in range(1, n+1):
#     print("*"*i + " "*(2*(n-i)) + "*"*i)
# for i in range(n, 0, -1):
#     print("*"*i + " "*(2*(n-i)) + "*"*i)


# n = 5
# for i in range(n):
#     print("* " * n)

# n = 5
# for i in range(1, n+1):
#     print("* " * i)



# n = 5
# for i in range(n, 0, -1):
#     print("* " * i)

# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i) + "* "*i)


# n = 5
# for i in range(n, 0, -1):
#     print(" "*(n-i) + "* "*i)


# n = 5
# for i in range(n, 0, -1):
#     print("*" * i)
# for i in range(2, n+1):
#     print("*" * i)


# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i) + "* "*i)


# n = 4
# for i in range(n, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# n = 4
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     print()


# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         if j == 1 or j == i or i == n:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# n = 4
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n-1, 0, -1):
#     print(" "*(n-i), end="")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# n = 4
# for i in range(n, 0, -1):
#     print(" "*(n-i), end="")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(2, n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# n = 5
# for i in range(n):
#     num = 1
#     print(" "*(n-i), end="")
#     for j in range(i+1):
#         print(num, end=" ")
#         num = num * (i-j) // (j+1)
#     print()



n = 5
for i in range(1, n+1):
    print("* " * i)
for i in range(n-1, 0, -1):
    print("* " * i)



















