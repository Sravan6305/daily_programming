# Take two inputs from user a and b and find the sum from a to b
# For example a = 0 and b= 5

a = int(input('enter a number: '))
b = int(input('enter a number: '))
total = 0
for x in range(a, b+1):
    total = total + x
print(total)