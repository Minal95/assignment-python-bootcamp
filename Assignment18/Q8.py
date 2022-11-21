# 8. Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.

list1=[1,2,3]
list2=["maggie","noodles","pizza"]
d={}
for i in range(0,len(list1)):
    d[list1[i]]=list2[i]
print(d)
