#Write a python script to generate Fibonacci terms using generator function.

def fib(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

n = int(input("Enter how many terms: "))
print("Fibonacci sequence:", fib(n))

