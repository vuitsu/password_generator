import random
import string

def generate_password(length, include_uppercase, include_numbers, include_special_characters):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    password_chars = lowercase
    if include_uppercase:
        password_chars += uppercase
    if include_numbers:
        password_chars += digits
    if include_special_characters:
        password_chars += special_characters
    return "".join(random.choice(password_chars) for i in range(length))

length = int(input("Enter the desired length for the password : "))
include_uppercase = input("Include uppercase letters (y/n) : ").lower() == 'y'
include_numbers = input("Include numbers (y/n) : ").lower() == 'y'
include_special_characters = input("Include special characters (y/n) : ").lower() == 'y'

password = generate_password(length, include_uppercase, include_numbers, include_special_characters)
print("Le mot de passe pour le compte généré est : " + password)