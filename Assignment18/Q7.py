# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

d1={"name1":"Minal","name2":"Sushma","name3":"Nisha"}
d2={"age1":23,"age2":22,"age3":24}
d3={"gender1":"female","gender2":"female","gender3":"female"}
d4={1:d1, 2:d2, 3:d3}
print(d4)