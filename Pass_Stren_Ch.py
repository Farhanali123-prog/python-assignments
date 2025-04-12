def password_strength_checker(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    symbols = "!@#$%^&*()_+-=[]{},.<>?/\\|~`"

    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
        elif 'a' <= char <= 'z':
            has_lower = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in symbols:
            has_symbol = True

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

# Main
password = input("Enter your password: ")
result = password_strength_checker(password)
print("Password Strength:", result)
