# Smart Bill Splitter (math + if + function)
# Write a function split_bill(total, people, tip_percent, is_weekend):
# Add tip
# If weekend, add extra 2% service charge
# Return per person amount, rounded to 2 decimals


def split_bill(total, people, tip_percent, is_weekend):
    tip = total * tip_percent
    total_amount = total + tip

    if is_weekend:
        total_amount += total*2 / 100

    return round(total_amount / people, 2)

print(split_bill(1000,4,10,True))
print(split_bill(2500,8,10,False))