a = int(input('enter the number: '))
b = int(input('enter the numbers: '))
c = int(input('enter the numbers: '))

# if a >= b and a >= c:
#     print(f'maximum number is {a}')
# elif b >= a and b >= c:
#     print(f'maximum number is {b}')
# else:
#     print(f'maximum number is {c}')

if a <= b and a <= c:
    print(f'minimum number is {a}')
elif b <= a and b <= c:
    print(f'minimum number is {b}')
else:
    print(f'minimum number is {c}')