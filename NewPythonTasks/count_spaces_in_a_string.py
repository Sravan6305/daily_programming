# WAP to count the number of spaces in a string.

string = input('enter any word with or without any spaces: ')
count = 0
for x in string:
    if x == ' ':
        count = count + 1
print(count)