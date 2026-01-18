# Find the shortest character in a string. for ex- "bcdaef" -> 'a'.
# Find the largest character in a string. for ex- "bcdaef" -> 'f'.

string = input("Enter a string: ")

shortest = string[0]
largest = string[0]

for ch in string:
    if ch < shortest:
        shortest = ch
    if ch > largest:
        largest = ch

print(f"Shortest character: {shortest}")
print(f"Largest character: {largest}")
