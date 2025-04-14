
import string
import random

def generate_password(length=12):
    if length < 4:
        return "pass length should not be less than 4"

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()"

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = uppercase + lowercase + digits + symbols
    password = password + random.choices(all_chars, k=length-1)

    random.shuffle(password)

    return ''.join(password)

print("Password: ", generate_password(20))

