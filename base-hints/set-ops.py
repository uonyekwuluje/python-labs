# Basic Set Operations. Can also be instantiated by
# var = set()
A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}

print("===================================")
print(f"Set A => {A}\nSet B => {B}")
print("===================================")
print(f"The Union of {A} and {B} => {A | B}")  # Elements in either set A or set B (or both).
print(f"The Intersection of {A} and {B} => {A & B}") # Elements common to both set A and set B.
print(f"The Difference between {A} and {B} => {A - B}") # Elements in set A but not in set B.
print(f"The Symmetric Difference between {A} and {B} => {A ^ B}") # Elements in either set A or set B, but not in both.

A.add(9) # Add element to a set
print(A)
