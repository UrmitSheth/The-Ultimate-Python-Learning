s1 = {1,2,3,4}
s2 = {3,4,5,6}

# 1. Union of two sets
union_set = s1.union(s2)
print("Union: ", union_set)

# 2. Intersection of two sets
intersection_set = s1.intersection(s2)
print("Intersection: ", intersection_set)

# 3. Difference of two sets
difference_set = s1.difference(s2)
print("Difference (s1 - s2): ", difference_set)
difference_set = s2.difference(s1)
print("Difference (s2 - s1): ", difference_set)

# 4. Symmetric Difference of two sets
symmetric_difference_set = s1.symmetric_difference(s2)
print("Symmetric Difference: ", symmetric_difference_set)


s3 = {1, 2, 3, 4, 5, 6}
s4 = {3, 4, 5, 6}

# 5. Checking if a set is a subset of another
is_subset = s4.issubset(s3)
print("Is s4 a subset of s3? ", is_subset)
print({1, 2}.issubset({1, 2, 3})) # True

# 6. Checking if a set is a superset of another
is_superset = s3.issuperset(s4)
print("Is s3 a superset of s4? ", is_superset)


s5 = {1, 2, 3}
s6 = {4, 5, 6}

# 7. Checking if two sets are disjoint
are_disjoint = s5.isdisjoint(s6)
print("Are s5 and s6 disjoint? ", are_disjoint)

