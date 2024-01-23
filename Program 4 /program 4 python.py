numbers = [1, 2, 3, 4, 5]
if not numbers:
 print("List is empty. Cannot calculate average.")
else:
 avg = sum(numbers) / len(numbers)
 print(f"The average of the numbers is: {avg}")
