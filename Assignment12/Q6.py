# 6. Write a python script to print first N prime numbers



N=int(input("Enter N : "))

for num in range(1,2*N+1):
    count=0
    for i in range(2,(num//2+1)):
        if(num%i==0):
            count=count+1
            break
    if(count==0 and num!=1):
        print("%d"%num)