# Check two strings are equal or not. IGNORE THE CASE.
# for ex- "abcde" is same as "AbCdE".

string1 = input('enter a word: ')
string2 = input('enter a word: ')

if string1.lower() == string2.lower():
    print('they are equal')
else:
    print('they are not equal')