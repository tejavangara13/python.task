# Assignemnt question:
# Count the number of swaps performed by bubble sort while sorting an array.
# Apply binary search in only first half of the list. (Search only in first half)

def bubble_sort_with_swaps(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_count += 1
    return swap_count, arr

arr = [5, 3, 2, 4, 1]
swaps, sorted_arr = bubble_sort_with_swaps(arr)
print("Sorted Array:", sorted_arr)
print("Number of Swaps:", swaps)


def binary_search_first_half(arr, target):
    left = 0
    right = len(arr)//2   

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print("Index:", binary_search_first_half(arr, target))