num=int(input("Enter a number:"))
order=len(str(num))
sum_of_power=sum(int(digit)** order for digit in str(num))
if num==sum_of_power:
    print(num,"Is an Armstrong number")
else:
    print(num,"Is not an Armstrong number")  
      