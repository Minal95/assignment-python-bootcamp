#Write a python script to print all Prime numbers under 100
n=1
while n<=100:
    i=2
    while
    if n%i==0:
        break
    i+=1
else:
    print(i, end=' ')
     



n=int(input("Enter a number to check wheter it is prime or not:"))
r=range(2,int(n/2)+1)
for i in r:
    if n%i==0:
        print(n,"it is not a prime number")
        break
else:
    print(n,"is a prime number")