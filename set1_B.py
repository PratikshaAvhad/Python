# Write a program to accept a number and count number of even, odd, zero digits
#within that number.

num = input("Enter a number: ")
even_count = 0
odd_count = 0
zero_count=0
for digit in num:
    if digit.isdigit():  
        d = int(digit)
        if d == 0:
            zero_count += 1
        elif d % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

print(f"Even digits: {even_count}")
print(f"Odd digits: {odd_count}")
print(f"Zero digits: {zero_count}")

# Write a program to accept a binary number and convert it into decimal number.

binary_num = input("Enter a binary number: ")
decimal_num = int(binary_num, 2)
print(f"Binary number {binary_num} in decimal is {decimal_num}")

#Write a program which accepts an integer value as command line and print “Ok”
#if value is between 1 to 50 (both inclusive) otherwise it prints ”Out of range”


print("*****************************************************")

#4. Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’.

n = int(input("Enter a number: "))

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

#5. Write python script to accept two numbers as range and display multiplication table of all
#numbers within that range.

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for num in range(start, end + 1):
    print(f"\n Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")






















