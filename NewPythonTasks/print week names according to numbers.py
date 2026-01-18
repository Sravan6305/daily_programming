# Take a number from user
# If the number is between 1 and 7 then print the days of the week accordingly
# For example - if user gives 1 then print Monday if 2 print Tuesday and so on
# And if the user gives any number less than 1 or greater than 7 then print "Invalid Number"

n = int(input('enter the number: '))

if n == 1:
    print('monday')
elif n == 2:
    print('tuesday')
elif n == 3:
    print('wednesday')
elif n == 4:
    print('thursday')
elif n == 5:
    print('friday')
elif n == 6:
    print('saturday')
elif n == 7:
    print('sunday')
else:
    print('invalid number')