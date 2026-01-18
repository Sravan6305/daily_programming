# Write a python program that takes the user to provide a single character from the alphabet.
# Print Vowel or Consonant, depending on the user input.

letter = input('enter the letter: ')

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print('vowel')
else:
    print('consonant')