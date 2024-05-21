# problem 3
"""
Problem Statement:

Prompt the user to enter a sentence.
Ask user to replace the word
ask user to replace the word with

Print the modified sentence
"""
# SOLUTION

sentence = input("Enter a sentence:")
old = input("Enter the word you want to replace:")
new = input("Enter the new word:")
update = sentence.replace(old, new)
print(update)