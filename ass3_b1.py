#Write a Python program to create set difference and a symmetric difference.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set1:", set1)
print("Set2:", set2)

diff = set1.difference(set2)
print("Difference (Set1 - Set2):", diff)

sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)


