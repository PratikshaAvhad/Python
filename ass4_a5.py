#Write generator function which generate even numbers up to n

def even_numbers(n):
    for i in range(2, n+1, 2):  
        yield i


n = int(input("Enter a number: "))
print("Even numbers up to", n, ":")
for num in even_numbers(n):
    print(num, end=" ")
