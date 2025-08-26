marks = {
    "Urmit": 100,
    "Hardik": 56,
    "Dev": 23,
    0: "Akshay"
}
# 1.  
# print(marks.items())
# 2. 
# print(marks.keys())
# 3.
# print(marks.values())

# 4. Adding Entries____
# marks.update({"Dev": 99, "Saurav": 70} )


# 5.   ## Returns the value associated with the key "Urmit" ## 
# print(marks.get("Urmit"))
# 6.  ## Returns the value associated with the key 0 ##
# print(marks["Urmit"])

# print(marks.get(1)) # Prints None
# print(marks[1]) # Returns an error

# 7. Adding a new key-value pair
marks["Add_value"] = "Added_vale" 

# 8. Removing Entries_____
# marks.pop("Add_value")
# 9.
# del marks[0]

# 10. ## Removes the last inserted key-value pair ##
# marks.popitem()

# 11. copying the dictionary
# new_marks = marks.copy()
# print(new_marks)

# 12. Creating a new dictionary with keys from a list
keys = ['a', 'b', 'c', 'd']
d = dict.fromkeys(keys,0)  # Creates a new dictionary with keys from the list and values set to 0
print(d)

# 13. Setting default values for keys
c = {}
c.setdefault("key1", "value1") # Adds key1 with value1 if key1 does not exist
print(c)

# 14. Clearing the dictionary
marks.clear()
print(marks) # This will print an empty dictionary
