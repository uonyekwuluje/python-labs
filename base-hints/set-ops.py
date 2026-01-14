# Basic Set Operations. Can also be instantiated by
# var = set()
A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}

print("===================================")
print(f"Set A => {A}\nSet B => {B}")
print("===================================")
print(f"The Union of {A} and {B} => {A | B}")
print(f"The Intersection of {A} and {B} => {A & B}")
print(f"The Difference between {A} and {B} => {A - B}")
print(f"The Symmetric Difference between {A} and {B} => {A ^ B}")
