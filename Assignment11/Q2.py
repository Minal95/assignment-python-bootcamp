#Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter value of n: "))
sum=0
r=range(1,n+1)
for x in r:
    sum=(sum+x**2)
print("The sum of squares of first" ,n, " natural number is : ",sum)