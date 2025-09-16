# Sorting
list1=[10,-3,700,45,23,100,-300]
for j in range(0,6):
    for i in range(0, len(list1)-1):
        if list1[i]>list1[i+1]:
         list1[i],list1[i+1]=list1[i+1],list1[i]
    print(list1)        

#Bubble Sort for Descending Order
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Bubble Sort to Sort Strings Alphabetically
nums = [5, 1, 4, 2, 8]
print("Descending:", bubble_sort_desc(nums))


def bubble_sort_strings(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


words = ["siva", "sai", "ram", "krishna"]
print("Strings:", bubble_sort_strings(words))

#Bubble Sort Strings by Length
def bubble_sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(arr[j]) > len(arr[j+1]):  
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


words = ["teja", "saira", "srivalli", "parveen"]
print("By length:", bubble_sort_by_length(words))

#Sort Nested Lists by First Element
def bubble_sort_nested(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][0] > lst[j+1][0]:  
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


nested = [[3, "c"], [1, "a"], [4, "d"], [2, "b"]]
print("Nested:", bubble_sort_nested(nested))





