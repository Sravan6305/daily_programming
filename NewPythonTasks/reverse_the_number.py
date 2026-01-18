# A five-digit number is entered through the keyboard.
# Write a program to obtain the reversed number
# and to determine whether the original and reversed numbers are equal or not.

num = int(input("Enter a five-digit number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

if original == reverse:
    print("Original and reversed numbers are equal")
else:
    print("Original and reversed numbers are not equal")
