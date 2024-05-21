# problem 6
"""
Problem: Create a small program that asks the user for their first name and last name,
converts them to uppercase,
replaces spaces with hyphens
and calculates the length of their full name.

print 3 variables i.e
print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))

NOTE: Concepts Covered: input(), string methods (upper, replace), len(), print()
"""

# SOLUTION:

first_name = input("Enter your first name:")
first_name_upper = first_name.upper()
last_name = input("Enter your last name:")
last_name_upper = last_name.upper()

full_name_upper = first_name_upper + " " + last_name_upper
modified_sentence = full_name_upper.replace(" ", "-")

full_name_length = len(full_name_upper)

print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))