import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

try:
    length = int(input("What is your desired length of password? "))
    password = "".join(random.sample(letters + numbers + symbols, length))
    print("Your randomly generated password: " + password)
except ValueError:
    print("Invalid input. Please enter a number.")