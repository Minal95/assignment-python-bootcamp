#Write a Python script to remove all non int values from a list.


list=[25,"minal",7,67.8,True,4]
b=[]
for i in list:
    if type(i)==int:
        b.append(i)
    else:
        pass
print(b)


