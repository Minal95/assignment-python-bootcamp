#Write a python program to Sort a tuple of tuples by the second item.
#tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))


tuple1=(('a', 21),('b', 37),('c', 11), ('d',29))
print("Original List: ", tuple1)
def Sort(tuple):
    #reverse=None (Sorts in Ascending order)
    return(sorted(tuple1, key= lambda a: a[1]))
print("Sorted List:", Sort(tuple1))
    
