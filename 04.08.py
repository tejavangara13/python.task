#keyword arbitary arguments

# def connect_to_db(*args):
#     print(args)
# connect_to_db('localhost:3000','2345','3300','2243')


# def connect_to_db2(**kargs):
#     print(kargs)
#     print(type(kargs))
# connect_to_db2(db_loc='localhost:3000',db_pool='2345',db_port='3300',db_password='2243')



# def add(num1,num2):
#     print(num1+num2)
# add(2,5)
# def add2(num1,num2):
#     return num1+num2
# result=add2(2,5)
# print(add2(4,5))
# print(result)
# print(result*5) 


#return statement once exicuted

# def even_or_odd(n1):
#     if n1%2==0:
#         return 'Even'
#     else:
#         return'Odd'
# r1=even_or_odd(25) 
# print(r1)


# def simple_calculator(a,b):
#     return a+b,a-b,a*b
# r2=simple_calculator(2,5)
# print(r2)
# print(type(r2))

# def check(num):
#     if num>0:
#         print('pos')
#     elif num==0:
#         print('zero')
#     else:
#         print('negative')
# num_input=int(input('enter a no:'))
# check(num_input)


# this program is a terinary operator
# def even_or_odd(num1):
#     res='even' if num1%2==0 else 'odd'
#     print(res)
# even_or_odd(5)

# def vote(age):
#     res='vote'if age>=18 else 'notvote'
#     print(res)
# vote(13)

# def greater(n1,n2):
#     return n1 if n1>n2 else n2
# print(greater(3,4)) 

# def calci(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     if b!=0:
#       print(a%b)
#       print(a/b)
#     else:
#        print('zero divisble error')
#     print(a**b)
# calci(2,3)   
# another method
def simple_calc(n1,n2,op):
    if op=='+'or op=='add':
        print(n1+n2)
    elif op=='-' or op=='sub':
        print(n1-n2)
    elif op=='*'or op=='mul':
        print(n1*n2)
    elif op=='/'or op=='div':
        print(n1/n2) if n2!=0 else print('not possible')
    else:
        print('invalid input')

num1=int(input('enter a no 1:'))
num2=int(input('enter a no 2:'))
input_op=input('enter operation:')
(simple_calc(num1,num2,input_op))

