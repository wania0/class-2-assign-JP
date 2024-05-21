# problem 5
"""
Write a program that:

Asks the user to enter their full name.
Converts the full name to uppercase and prints it.
Asks the user for their favorite number.
Multiplies the number by 2, converts it to a string, and concatenates it to a message.

Prints the message "Your favorite number multiplied by 2 is X.", where X is the new number.
"""

# SOLUTION

name = input("Enter your full name:")
print("Your name in upper case is:", name.upper())
number = int(input("Enter your favourite number:"))
fav = number * 2
new = str(fav)
message = "Your favourite number multiplied by 2 is:"
print(message + new)