n=5
for i in range(n):
    for j in range(n):
        if i+j <= n-1 or i==j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 


n=7
for i in range(n):
    for j in range(n):
        if i+j > n-1 or i==j:
         print('*', end=' ')
        else:
         print(' ', end=' ')
    print()     
#A
n = 7
for i in range(n):
    for j in range(n):
        if (j == 0 or j == n-1) and i != 0 or (i == 0 and j > 0 and j < n-1) or (i == n//2):
            print("A", end=" ")
        else:
            print(" ", end=" ")
    print()


n = 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

#C
n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0:
            print("C", end=" ")
        else:
            print(" ", end=" ")
    print()

#D
n = 7  

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("D", end=" ")
        else:
            print(" ", end=" ")
    print()


#E
n = 7
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n - 1 or i == n // 2:
            print("E", end=" ")
        else:
            print(" ", end=" ")
    print()

#F
n = 7
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == n // 2:
            print("F", end=" ")
        else:
            print(" ", end=" ")
    print()

#H
n = 7
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == n // 2:
            print("H", end=" ")
        else:
            print(" ", end=" ")
    print()

#I
n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == n // 2:
            print("I", end=" ")
        else:
            print(" ", end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
    print()     


n=5
for i in range(n):
    for j in range(n):
        if i>j:
            print("*",end=" ")
    print() 



n=5
for i in range(n):
    for j in range(n):
        if i<j:
            print("*",end=" ")
    print()     



n=7
for i in range(n):
    for j in range(n):
        if i+j > n-1:
         print('*', end=' ')
        else:
         print(' ', end=' ')
    print()  



n=7
for i in range(n):
    for j in range(n):
        if i+j < n-1:
         print('*', end=' ')
        else:
         print(' ', end=' ')
    print()      
           

n=7
for i in range(n):
    for j in range(n):
        if i+j - n-1:
         print('*', end=' ')
        else:
         print(' ', end=' ')
    print() 


n=7
for i in range(n):
    for j in range(n):
        if i+j + n-1:
         print('*', end=' ')
        else:
         print(' ', end=' ')
    print()  


n=9
for i in range(n):
    for j in range(n):
        if i+j < n-1:
         print('*', end=' ')
        else:
         print(' ', end=' ')
    print()                      

          