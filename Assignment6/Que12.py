x=complex(input("Enter a complex number:"))
print(x)
print(x.real if x.real>x.imag else x.imag)