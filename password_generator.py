import random
import string

def generate_password(length):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(length):
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Medium"
    else:
        return "Strong"

print("   Secure Password Generator")

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
            continue

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        print("\nPassword Strength:", check_strength(length))

        choice = input("\nGenerate another password? (y/n): ").lower()

        if choice != 'y':
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")