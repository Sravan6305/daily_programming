# Reverse the first half of the string.

s = input("Enter a string: ")

half = len(s) // 2
first = s[:half]
second = s[half:]

print(first[::-1] + second)
