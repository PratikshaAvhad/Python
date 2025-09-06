#Write a generator function which generates prime numbers up to n

def primes(n):
    prime_list = []
    for num in range(2, n+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            prime_list.append(num)
    return prime_list

n = int(input("Generate primes up to: "))
print("Prime numbers up to", n, ":", primes(n))
