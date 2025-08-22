Tuple = ( 1, 22, 3.14, "Hello",True) # tuple is immutable

# Tuple.append("item")  --- not allowed
# Tuple.remove("item") --- not allowed
print(Tuple)
print(type(Tuple))

Changeable = list(Tuple) 
print(Changeable)
print(type(Changeable)) # List is mutable

Changeable.append("new item") # allowed
print(Changeable)

#########################################################

Tuple[2] = 3.14159 # not allowed, tuples are immutable
