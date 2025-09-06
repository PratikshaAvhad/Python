# Define a function that accept two strings as input and find union and intersection of them.

def union_intersection(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    union = set1.union(set2)
    intersection = set1.intersection(set2)

    print("Union:", union)
    print("Intersection:", intersection)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

union_intersection(s1, s2)
