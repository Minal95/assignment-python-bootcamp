year=int(input("Enter year number:"))
if year%400==0 or year%100!=0 and year%4==0:
    print("Tihs is a Leap year")
else:
    print("This is not a Leap year")
