#Write a Python program to create a list of tuples with the first element as the number and second 
#element as the square of the number.

numbers = [1, 2, 3, 4, 5]

result = [(n, n**2) for n in numbers]

print("List of tuples (number, square):", result)
