#Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter value of n: "))
sum=0
r=range( 2,n+1,2)

for x in r:

    sum=sum+x
print("The sum of first" ,n, " even natural number is : ",sum)
