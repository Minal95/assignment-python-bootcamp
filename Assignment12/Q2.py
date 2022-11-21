#Write a python script to check whether a given number is Prime or not
n=int(input("Enter a number to check wheter it is prime or not:"))
r=range(2,int(n/2)+1)
for i in r:
    if n%i==0:
        print(n,"it is not a prime number")
        break
else:
    print(n,"is a prime number")