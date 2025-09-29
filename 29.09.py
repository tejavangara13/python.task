
# 1.Print list in a reverse order 
# 2.Print exponent of two numbers without using double star operator & loops

# Method 1: Using slicing
my_list = [10, 20, 30, 40, 50]
print("Reversed List (slicing):", my_list[::-1])

# Method 2: Using reversed()
print("Reversed List (reversed()):", list(reversed(my_list)))


def power(base, exp):
    # Base case
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# Example
print("2^5 =", power(2, 5))
print("3^4 =", power(3, 4))

