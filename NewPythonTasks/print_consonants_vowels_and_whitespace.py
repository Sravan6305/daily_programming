# Write a program to find the number of vowels, consonents, digits and white space characters in a string.

word = input('enter any word: ')
count1 = 0
count2 = 0
count3 = 0
if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
    count1 = count1 + 1
elif word == ' ':
    count2 = count2 + 1
else:
    count3 = count3 + 1

print(count1)
print(count2)
print(count3)