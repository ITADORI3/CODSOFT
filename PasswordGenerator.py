import random
import string

def generate_password(length, num_caps, num_small, num_special, num_digits):
    caps = ''.join(random.choice(string.ascii_uppercase) for _ in range(num_caps))
    small = ''.join(random.choice(string.ascii_lowercase) for _ in range(num_small))
    special = ''.join(random.choice("!@#$%&*.") for _ in range(num_special))
    digits = ''.join(random.choice(string.digits) for _ in range(num_digits))

    remaining_length = length - (num_caps + num_small + num_special + num_digits)
    chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(remaining_length))

    password = caps + small + special + digits + chars
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    return shuffled_password

print("Hey there! Let's create a customized password.\n")
length = int(input("Enter the total length of the password:\n"))
num_caps = int(input("How many uppercase letters would you like?\n"))
num_small = int(input("How many lowercase letters would you like?\n"))
num_special = int(input("How many special characters would you like?\n"))
num_digits = int(input("How many digits would you like?\n"))

if length < (num_caps + num_small + num_special + num_digits):
    print("Error: The sum of requested characters exceeds the password length.")
else:
    password = generate_password(length, num_caps, num_small, num_special, num_digits)
    print("\nYour customized password is:", password)
