# 4. Write a python script to print all Prime numbers between two given numbers (both
# values inclusive)

num1=int(input("Enter num1 : "))
num2=int(input("Enter num2 : "))

total=0
for num in range(num1,num2+1):
    count=0
    
    for i in range(2,(num//2)+1):
        if(num%i==0):
           count=count+1
           break

    if(count==0 and num!=1):
        print("%d"%num,end=' ')
        total=total+1
   
print("\nTotal prime number between %d to %d is %d"%(num1,num2,total))
             

 