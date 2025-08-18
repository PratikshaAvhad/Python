#1)cashier has currency notes of denomination 1, 5 and 10. Write python script to accept the amount to 
#be withdrawn from the user and print the total number of currency notes of each denomination the 
#cashier will have   to give. 
# Accept the amount from the user
amount = int(input("Enter the amount to withdraw: "))

ten_notes = amount // 10 #convert in integer
amount = amount % 10

five_notes = amount // 5
amount = amount % 5

one_notes = amount

print("10 rupee notes:", ten_notes)
print("5 rupee notes :", five_notes)
print("1 rupee notes :", one_notes)
print("*********************************************************")

#2)Write a python script to accepts annual basic salary of an employee and calculates and displays the 
#Income tax as per the following rules.  
#Basic:  < 2,50,000  
#Tax = 0
# Basic: 2,50,000 to 5,00,000 Tax = 10%  
 # Basic: > 5,00,000  Tax = 20%

basic_salary = float(input("Enter annual basic salary: "))

if basic_salary < 250000:
    tax = 0
elif basic_salary <= 500000:
    tax = basic_salary * 0.10
else:
    tax = basic_salary * 0.20

print("Income Tax =", tax)
print("*********************************************************")

#Write python script to accept the x and y coordinate of a point and find the quadrant in
#which the point lies.
# Accept coordinates from user
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("The point lies in the First Quadrant.")
elif x < 0 and y > 0:
    print("The point lies in the Second Quadrant.")
elif x < 0 and y < 0:
    print("The point lies in the Third Quadrant.")
elif x > 0 and y < 0:
    print("The point lies in the Fourth Quadrant.")
elif x == 0 and y == 0:
    print("The point lies at the Origin.")
elif x == 0:
    print("The point lies on the Y-axis.")
elif y == 0:
    print("The point lies on the X-axis.")
print("*********************************************************")
#Write a python script to accept the cost price and selling price from the keyboard.
#Find out if the seller has made a profit or loss and display how much profit or loss has been made. 

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit of {profit}")
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"Loss of {loss}")
else:
    print("No profit, no loss.")

print("*********************************************************")
