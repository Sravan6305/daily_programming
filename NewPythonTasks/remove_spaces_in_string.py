# WAP to remove all the spaces in a string.

string = input('enter a string: ')
a = string.split(' ')
for x in a:
    print(x ,end = '')