# 5. Write a python script to find next prime number of a given number


num1=int(input("Enter number : "))

for num in range(num1,10):
    count=0
    for i in range(2,(num//2)+1):
        if(num%i==0):
            count=count+1
            break

    if (count==0 and num!=1):
        print("%d"%num)