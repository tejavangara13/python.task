# n=5
# for i in range(n):
#     start=i+1
#     for sp in range(2* (n-i-1)):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print(start, end=" ")
#         start-=1
#     print()
 

# s = "(a+b-c*[e/f])"
# result = ""
# for ch in s:
#     if ch not in "()[]{}":
#         result += ch
# print(result)   # Output: a+b-c*e/f




# s = "Hello"

# # Method 1: Using slicing
# print(s[::-1])

# # Method 2: Using reversed() and join
# print("".join(reversed(s)))

# # Method 3: Using loop
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)

# # Method 4: Using recursion
# def reverse_str(st):
#     if len(st) == 0:
#         return st
#     return reverse_str(st[1:]) + st[0]
# print(reverse_str(s))


s = "Hello World"
vowels = consonants = spaces = 0
for ch in s.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch == " ":
        spaces += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)



       