# sets in python:
empty_set = set() # create an empty set with peranthesis set() 
print(type(empty_set))

set_1 = {1,2,2,3,4,4,5}
print(f"unique values: {set_1}") # allow only unique values

# calculate length of set
print(f"length of set is = {len(set_1)}")

#check and print the type of set
print(f"type of set is : {type(set_1)}")

# add method is used to add the elements in set
set_1.add(6)
print(f"add an element in set: {set_1}")