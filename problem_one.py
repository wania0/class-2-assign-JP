# problem 1
"""
Problem Statement:
Prompt the user to enter a float number.
Use the round() function to round the number to 2 decimal places.
Print the original number and the rounded number.
Use the len() function to find the length of a string entered by the user and print the result.
"""
# SOLUTION
user_input = input("Enter a float number in string format:")
float_input = float(input("Enter a float number:"))
rounded_value = round(float_input, 2)
print("The original number is:", float_input, "\nThe rounded number is:", rounded_value)
len_input = len(user_input)
print("The length of a string entered by the user is:", len_input)