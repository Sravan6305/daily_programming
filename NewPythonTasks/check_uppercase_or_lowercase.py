# Write a program to check whether a entered character is lowercase ( a to z ) or uppercase ( A to Z ).

character = input("Enter a character: ")

if character <= 'a' and character <= 'z':
    print("The entered character is lowercase")
elif character >= 'A' and character >= 'Z':
    print("The entered character is uppercase")
else:
    print("Not an alphabet character")
