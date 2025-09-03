# # num1=2451
# # temp=num1
# # rev_num=0
# # while num1>0:
# #     digit=num1%10
# #     rev_num=rev_num*10+digit
# #     print(digit)
# #     num1=num1//10
# # print(rev_num)    


# #assignment
#   #print even digits
#   # print prime digits in a given number  


# #swapping=> 
# num1=10
# num2=20
#  #Method 1
# # num1,num2=num2,num1
# #Method
# temp=num2
# num2=num1
# num1=temp
# print(num1,num2)

# #Method 3
# num1=10
# num2=20

# num1=num1+num2#num1=30
# num2=num1-num2#num2=10
# num1=num1-num2#num1=20

# #Method 4- XOR properties
# #1 property =>
# x=5
# print(x^x)
# print(x^0)

num = 49368257
print("Number:", num)

digits = [int(d) for d in str(num)]   # convert to list of digits
even_digits = [d for d in digits if d % 2 == 0]

print("Even digits:", even_digits)



