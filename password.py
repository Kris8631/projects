

password = input("Write your password: ")


has_lower = False
has_upper = False
has_digit = False
for char in password:
    if char.isalpha() and char.isupper():
        has_upper = True
    if char.isalpha() and char.islower():
        has_lower = True
    if char.isdigit():
        has_digit = True

long_enough = len(password) >= 8 

is_correct = has_lower and has_upper and has_digit and long_enough
if is_correct:
    print("Your password is complex enough")
else:
    print("Change following elements in your password:")
    if not has_lower:
        print("- at least one lowercase letter")
    if not has_upper:
        print("- at least one capital letter")
    if not has_digit:
        print("- at least one digit")
    if not long_enough:
        print("- at least eight signs")