import random

def generate_password(length):
    # Define the character sets
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*()-_=+[]{}|;:,.<>?'

    # Combine all character sets
    all_characters = upper_case + lower_case + digits + symbols

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")

    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")

# Run the main function
main()