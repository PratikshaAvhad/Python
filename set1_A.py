# 1)Write python script to calculate sum of digits of a given input number.
num = int(input("Enter a number: "))
num = abs(num)
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10

print("Sum of digits =", sum_digits)

#2)Write python script to check whether a input number is Armstrong number or not. 

num = int(input("Enter a number: "))
original_num = num

num_digits = len(str(num))

sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** num_digits
    num //= 10

if sum== original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

# 3)Write python script to check whether a input number is perfect number of not. 
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")

#4)Write a program to calculate XY

x = float(input("Enter value of X: "))
y = float(input("Enter value of Y: "))

result = x ** y

print(f"{x} raised to the power {y} is {result}")

#5)Write a program to check whether a input number is palindrome or not.

num = int(input("Enter a number: "))

num_str = str(num)

if num_str == num_str[::-1]:
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")

#6)Write a program to calculate sum of first and last digit of a number.
 
num = int(input("Enter a number: "))

last_digit = num % 10

first_digit = num
while first_digit >= 10:
    first_digit //= 10

sum_digits = first_digit + last_digit

print(f"First digit: {first_digit}")
print(f"Last digit: {last_digit}")
print(f"Sum of first and last digit: {sum_digits}")


