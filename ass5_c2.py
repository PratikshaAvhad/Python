#Define datetime module that provides time object. Using this module write a program 
#that gets current date and time and print day of the week.

from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

day_index = now.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print("Today is:", days[day_index])
