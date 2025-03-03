# First, use set operations based on the given diagram -- define them
A = {"a", "g", "d", "f", "b", "c"}
B = {"b", "c", "h", "l", "m", "o"}
C = {"c", "h", "k", "j", "i", "d", "f"}

print("\na. How many elements are there in set A and B?")
A_union_B = A | B
print("Number of elements in A union B:", len(A_union_B)) 

print("\nb. How many elements are in B that are not part of A and C?")
B_not_in_A_C = B - (A | C)
print("Number of elements in B not in A or C:", len(B_not_in_A_C))

print("\nShow the following using set operations:")
# Assigning 
i = (C | (B & C)) - A    # Elements in C and B excluding A
ii = A & C  # Elements common between A & B or A & C
iii = B & (A | C)     # Elements in B that are also in A or C
iv = ( A & C ) - B            # Elements in both A and C
v = A & B & C          # Elements common in A, B, and C
vi = B - (A | C)    # Elements in B but not in A or C

# Print the results
print("i. [h, i, j, k]:", i)
print("ii. [c, d, f]:", ii)
print("iii. [b, c, h]:", iii)
print("iv. [d, f]:", iv)
print("v. [c]:", v)
print("vi. [l, m, o]:", vi)
