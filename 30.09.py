# fibinacci
# if a string is a palindrome
#binary search using recursion

#assignment questions
#max element in a list

# 0,1,1,2,3,5
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(6))




# def binary_search(arr, low, high, x):
#     if high >= low:
#         mid = (low + high) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid - 1, x)
#         else:
#             return binary_search(arr, mid + 1, high, x)
#     else:
#         return -1

# arr = [2, 4, 6, 8, 10, 12, 14]
# x = 10
# result = binary_search(arr, 0, len(arr)-1, x)

# if result != -1:
#     print("Element found at index:", result)
# else:
#     print("Element not found")


numbers = [12, 45, 23, 67, 89, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("Maximum element:", max_num)


