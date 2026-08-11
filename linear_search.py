# x = 10 find the index number of 10 and print -> basically linear search example
list_1 = [1,2,3,10,4]
x = 10
index = 0
for i in list_1:
    if i == x:
        print(f"{x} found at the index of: {index}")
        break
    index += 1