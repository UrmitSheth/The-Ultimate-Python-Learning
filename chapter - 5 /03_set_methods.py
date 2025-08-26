s = {1,2,3,4,5,6,6,7,7,7,8,8,8,8}

print(s,type(s))

# 1. Adding elements to a set
s.add(9)

# 2.update 
s.update([10,11,12]) # Adds multiple elements to the set

# 3. Removing elements from a set
s.remove(1) # Raises an error if the element is not found
s.discard(2) # Does not raise an error if the element is not found  

# 4. pop 
s.pop() # Remove any random element from the set

# 5. Checking if an element exists in a set
print(1 in s)

# 6. clearing a set
s.clear() # Removes all elements from the set

print(s,type(s))
