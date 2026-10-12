import string
import secrets

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    return "Strong"


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


print("=== Password Generator & Strength Checker ===")

password = input("Enter a password to check: ")
print("Password Strength:", check_strength(password))

choice = input("Generate a secure password? (yes/no): ")

if choice.lower() == "yes":
    print("Generated Password:", generate_password())
