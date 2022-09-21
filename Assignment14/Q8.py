#Write a Python script to print distinct elements along with their frequencies of
#occurrence in the list.


l1=["Minal",23,True,"Minal",45.6,5.6,45.6,8,23]

for e in l1:
    print("distinct element is=",e,"and frequencies of occurrence of",e,"in the list is=",l1.count(e))
