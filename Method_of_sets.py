# Set Methods->
set_1 = {1,2,3,4,5}
# 1. method add element
print(f"before add an element: {set_1}")
set_1.add(6)
print(f"after add an element in set: {set_1}")

# 2. Method remove an element from set
set_1.remove(2)
print(f"after remove 2 in the set: {set_1}")

# 3. Clear return an empty set
set_1.clear()
print(f"after clear set: {set_1}")

# 4 pop remove a value randomly in set
set_ab = {45,78,90,34,30}
set_ab.pop()
print(f"after pop: {set_ab}")

# 5 union return unique values between 2 sets
set_A = {1,2,3,4,5,6,7}
set_B = {6,7,8,9,10}
print(f"after union of two sets: {set_A.union(set_B)}")

# 6 intersection of two sets return only matching values 6,7
print(f"after intersection of set_A and Set_b: {set_A.intersection(set_B)}")