# Take string as input and print only the initials of them. for example-
# "Computer Science" -> "CS"

string = input('enter any string: ')

for x in string:
    if x == x.capitalize():
        print(x, end = '')