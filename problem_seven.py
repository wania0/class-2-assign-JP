# problem 7
"""
Problem: Ask the user to input two numbers.
Calculate their average
and print the average rounded to 2 decimal places.

NOTE: Concepts Covered: round(), input(), print(), type casting
"""

# SOLUTION:

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter first number:"))
average = (num_1 + num_2)/2
result = round(average, 2)
print("The average rounded to 2 decimal places is:", result)