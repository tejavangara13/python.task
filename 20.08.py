<<<<<<< HEAD
for num in range(100, 2001):
    temp = num         
    sum_val = 0
    digits = len(str(num))  

    while temp > 0:
        digit = temp % 10         
        sum_val += digit ** digits
        temp //= 10               

    if num == sum_val:
         print(num)

# Prime numbers between 100 and 2000

for num in range(100, 2001):
    if num > 1:  
        is_prime = True
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
         



  
=======
for num in range(100, 2001):
    temp = num         
    sum_val = 0
    digits = len(str(num))  

    while temp > 0:
        digit = temp % 10         
        sum_val += digit ** digits
        temp //= 10               

    if num == sum_val:
         print(num)

# Prime numbers between 100 and 2000

for num in range(100, 2001):
    if num > 1:  
        is_prime = True
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
         



  
>>>>>>> 59ce5998e579546a6183cf518fdcab6611b4274d
   