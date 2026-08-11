student_info = {
    "Name": "vishnu sharma",
    "age":18,
    "course":"BCA",
    "cgpa":7.5,
    "fav subject": "Python Programming"
}

# Methods of dictionaries 1. dictionary.keys
dict_keys = student_info.keys()
print(dict_keys)

# 2.dictionary.values(access values of keys)
dict_values = student_info.values()
print(dict_values)

# 3. items() access the both key value pairs
dict_items = student_info.items()
print(dict_items)

# 4. get() -> if we enter the wrong key return the none and program execute
print(student_info.get("cgpa2"))

print("end of code here")

# 5. update =({ This functions is used to add the new key:value pairs})
student_info.update  ({
    "city_name": "New Dehli",
})
print(student_info)

