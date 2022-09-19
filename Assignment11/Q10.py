'''Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)'''
n=int(input("enter a number : "))
a=''
while n>0:
    a=str(a)+str(n%8)
    n=int(n/8)
print(a)