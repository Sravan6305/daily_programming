def password_score(pw):
    score = 0

    if len(pw) >= 8:
        score += 1

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "@#$%&*!":
            has_special = True

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

pw = input("Enter password: ")
print(password_score(pw))