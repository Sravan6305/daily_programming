# Write a python program that reads an positive integer and count the number of digits the number has.

number = int(input('enter a positive number: '))
count = 0
for x in str(number):
    count = count + 1
print(count)