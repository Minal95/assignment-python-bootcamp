a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=(b**2)-(4*a*c)
if d>0:
    print("Roots are unequal and real")
elif d==0:
    print("Roots are equal and real")
else:
    print("Roots are imaginary")
