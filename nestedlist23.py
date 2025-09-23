# list1=[[11,22,33],
#    [44,55,66],
#    [77,88,99]]

# output=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(list1)):
#     for j in range(len(list1)):
#         list1[i][j]=0
# print(list1)        


# #diagonal elements=0
# list2=[[11,22,33],
#        [44,55,66],
#        [77,88,99]]
# for i in range(len(list2)):
#     for j in range(len(list2)):
#         if i==j:
#             list2[i][j]=0
# print(list2)            
# output=[[0,22,33],
#        [44,0,66],
#        [77,88,0]]

# write a code to convert diagonal elements to zero (left diagonal elements and right diagonal elements too ).


matrix=[
    [13,22,24],
    [19,54,34],
    [17,88,92],
]
n=len(matrix)
for i in range(n):
    matrix[i][i]=0
    matrix[i][n-i-1]=0
for row in matrix:
    print(row) 

s=[
    [1,3,9,2],
    [3,1,2,4],
    [1,7,9,2]
] 
rows=len(s) 
cols=len(s[0])
for i in range(min(rows,cols)):
    s[i][i]=0
    s[i][cols-1-i]=0   
print(s)   

      




