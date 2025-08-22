name = "urmitSheth"

print(len(name))
print(name.endswith("Sheth"))
print(name.startswith("urmit"))
print(name)
print(name.capitalize())

count = name.count("t")
print(count) 
print(name.find("t")) # returns the index of first occurrence of t

replaced_name = name.replace("urmit", "akshay")
print(replaced_name)
