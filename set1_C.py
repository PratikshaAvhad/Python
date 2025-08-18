# Write a python script to generate the following pattern upto n lines 
#      1 
#    1 2 1 
#   1 2 3 2 1 
# 1 2 3 4 3 2 1


n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    # leading spaces
    print("  " * (n - i), end="")

    # increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # new line




