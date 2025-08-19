#nested loop

# for class_no in range(1,11): 
#     for roll_no in range(1,31):
#       if roll_no%2==0:  
#          print('class',class_no,'roll',roll_no)

 

#tables

# for j in range(1,11):
#   for i in range(1,21):
#     print(j, 'X',i, '=', j * i)

# for class_no in range(1,11):
#   if class_no%2==0: 
#     for roll_no in range(1,31):
#        print('class',class_no,'roll',roll_no)


#converted to while loop
# class_no = 1
# while class_no <= 10:
#     if class_no % 2 == 0:
#         roll_no = 1
#         while roll_no <= 30:
#             print('class', class_no, 'roll', roll_no)
#             roll_no += 1
#     class_no += 1


i=1
while i<=3:
    j=1
    while j<=3:
        print(j,end=' ')
        j+=1
    print()
    i+=1 

          

