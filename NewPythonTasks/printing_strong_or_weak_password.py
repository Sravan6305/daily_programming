password = input('enter any password: ')

upper = 0
lower = 0
digit = 0
special = 0
score = 0

if len(password) >= 9:
    score = score + 1

for x in password:
    if x.isupper():
        upper += 1
    elif x.islower():
        lower += 1
    elif x.isdigit():
        digit += 1

score = score + upper + lower + digit + special

if score <= 2:
    print(f'{password} is Weak password')
elif score <= 4:
    print(f'{password} is Medium password')
else:
    print(f' {password} is Strong password')
