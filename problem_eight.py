# problem 8
"""
Problem: Ask the user to input a sentence.
Replace all spaces with underscores
and split the sentence into words.

NOTE: Concepts Covered: replace(), split(), input(), print()
"""

# SOLUTION

sentence = input("Enter a sentence:")
replaced = sentence.replace(" ", "-")
splitted = sentence.split()
print("The replaced sentence is:", replaced)
print("The splitted sentence is:", splitted)