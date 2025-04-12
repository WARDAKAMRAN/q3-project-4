import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# User input
num_passwords = int(input("Enter number of passwords to generate: "))
password_length = int(input("Enter password length: "))

print("\nGenerated Passwords:")
for _ in range(num_passwords):
    print(generate_password(password_length))