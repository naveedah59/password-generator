import random
import string

print("🔐 Welcome to the Password Generator!")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Define characters to use in the password
letters = string.ascii_letters  # a-z and A-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # Special characters like !, @, #

# Combine all character sets
all_characters = letters + digits + symbols

# Generate password
password = ''.join(random.choice(all_characters) for _ in range(length))

# Show the password
print(f"Your generated password is: {password}")
