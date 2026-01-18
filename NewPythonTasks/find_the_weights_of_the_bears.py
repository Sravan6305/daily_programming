# Bear Limak wants to become the largest of bears, or at least to become larger than his brother Bob.
# Right now, Limak and Bob weigh a and b respectively.
# It's guaranteed that Limak's weight is smaller than or equal to his brother's weight.
# Limak eats a lot and his weight is tripled after every year, while Bob's weight is doubled after every year.
# After how many full years will Limak become strictly larger (strictly heavier) than Bob?
# Input
# The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight of Limak
# and the weight of Bob respectively.
# Output
# Print one integer, denoting the integer number of years after which Limak will become strictly larger than Bob.

a = int(input("Enter Limak's weight: "))
b = int(input("Enter Bob's weight: "))

years = 0

while a <= b:
    a = a * 3
    b = b * 2
    years = years + 1

print(years)
