# password-generator-cli.py
import random, string
length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)
# password-generator-cli.py
import random, string
length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)
