# basic methods of lists
list1 = [1,2,3,4]
# 1. append method  append add element in the list at the end

print(f"before append: {list1}")
list1.append(5)
print(f"after append: {list1}")

# insert Method -> add an element between the list using index and value
list1.insert(2,20) 
print(f"after insert: {list1}")

# sort Method -> sort the list by default in increasing order

print(f"before sorting: {list1}")
list1.sort() 
print(f"after sorting incresing order : {list1}")

# sort the list in decreasing order: 

list1.sort(reverse = True) 
print(f"sorting in decreasing order: {list1}")

# reverse method reverse the list 

reverse_list = [1,2,3,6,8,9,10]
print(f"before reversing: {reverse_list}")
reverse_list.reverse()
print(f"after reversing: {reverse_list}")



