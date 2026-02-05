# Topics: functions, strings
# Write a function that:
# takes a string
# checks whether it is a palindrome
# Print result in main program

def is_palindrome(number):
    number = number.lower()
    reverse = number[::-1]

    if number == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"


number = input("Enter a number: ")
result = is_palindrome(number)
print(result)
