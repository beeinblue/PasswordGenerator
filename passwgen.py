import random

print('Password Generator')

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"

password_length = int(input('Enter the password length: '))
characters_length = int(input('Enter the number of characters to use: '))

for password in range(password_length):
    passwords = ''
    for i in range(characters_length):
        passwords += random.choice(characters)
    print(passwords)