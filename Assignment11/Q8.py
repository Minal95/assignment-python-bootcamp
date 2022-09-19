#Write a python script to calculate sum of digits of a given number
i=int(input("Enter a number:"))
sum=0
while i>0:
    sum=sum+i%10
    i=i//10
print("Sum of digits=",sum)    
    
