#  Print first n natural numbers using recursion.

def print_natural(n):
    if n == 0:
        return
    print_natural(n - 1)
    print(n, end=' ')
n = 5
print("First", n, "natural numbers:")
print_natural(n)

#  N natural numbers using recursion in reverse order
def print_natural_reverse(n):
    if n == 0:
        return
    print(n, end=' ')
    print_natural_reverse(n - 1)


print("\n\nFirst", n, "natural numbers in reverse:")
print_natural_reverse(n)


#  First n even numbers using recursion
def print_even(n):
    if n == 0:
        return
    print_even(n - 1)
    print(2 * n, end=' ')

print("\n\nFirst", n, "even numbers:")
print_even(n)
