'''Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)'''
n=int(input("enter a number : "))
a=''


while n>0:
    a=str(a)+str(n%2)
    n=int(n/2)

print(a)