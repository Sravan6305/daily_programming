# Take a number from user
# If the number is between 1 and 12 then print the month of the year accordingly
# For example - if user gives 1 then print January if 2 print February and so on
# And if the user gives any number less than 1 or greater than 12 then print "Invalid Month".

n = int(input('enter the number: '))

if n == 1:
    print('january')
elif n == 2:
    print('february')
elif n == 3:
    print('march')
elif n == 4:
    print('april')
elif n == 5:
    print('may')
elif n == 6:
    print('june')
elif n == 7:
    print('july')
elif n == 8:
    print('august')
elif n == 9:
    print('september')
elif n == 10:
    print('october')
elif n == 11:
    print('november')
elif n == 12:
    print('december')
else:
    print('invalid month')