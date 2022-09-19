#Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter value of n: "))
sum=0
r=range(1,n+1,2)

for x in r:

    sum=sum+x
print("The sum of first" ,n, "odd natural number is : ",sum)
