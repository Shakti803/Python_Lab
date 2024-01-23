year = int(input("Enter a year to check if it's a leap year: "))
leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
if leap_year:
 print(f"{year} is a leap year.")
else:
 print(f"{year} is not a leap year.")
