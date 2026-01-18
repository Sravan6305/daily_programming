# Write a program to input any character and check whether it is alphabet, digit or special character.

ch = input("Enter any character: ")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print("It is an alphabet")
elif '0' <= ch <= '9':
    print("It is a digit")
else:
    print("It is a special character")
