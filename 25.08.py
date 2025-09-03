#reverce
list1=[2,2,3,5,9]
list1.reverse()
print(list1)

#sort
list1=[1,-32,45,62,91,-321]
list1.sort(reverse=True)
print(list1)


list1=['apple','boll','dog','cat','elephent']
list1.sort(key=len)
print(list1)


# t1=(1,2,3,4,5)
# t1.index()
# print(t1)

list1=[1,4,5,6,7,8]
list3=list1

# list1[0]=10
# list1.append(5)
# print(list1)
# print(list2)

list3=list1.copy()
print(list3)
list1[1]=2
list1[3][0]=8
print(list3)
print(list1)