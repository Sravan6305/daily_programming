# A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student allowed to sit in exam or not.

classes = int(input('enter number of classes held: '))
attended = int(input('enter number of classes attended: '))

percentage = attended / classes * 100

if percentage < 75:
    print(f'you have {percentage}% and not allowed to write the exam')
else:
    print(f'you have {percentage}% and you can write the exam')