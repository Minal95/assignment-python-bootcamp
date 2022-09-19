#Write a python script to calculate factorial of a given number
n=int(input("enter a number : "))
fact=1
r=range(n,0,-1)
for x in r:
    fact=fact*x
print("factorial of a given number ",n,"is : ",fact)


    