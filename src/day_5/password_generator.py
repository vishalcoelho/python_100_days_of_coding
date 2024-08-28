import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator() -> str:
    """Generate a password"""
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = []
    idx_letters = random.sample(range(len(letters)), nr_letters)
    password += [letters[idx] for idx in idx_letters]
    idx_symbols = random.sample(range(len(symbols)), nr_symbols)
    password += [symbols[idx] for idx in idx_symbols]
    idx_numbers = random.sample(range(len(numbers)), nr_numbers)
    password += [numbers[idx] for idx in idx_numbers]

    # print(password)
    idx_password = random.sample(range(len(password)), len(password))
    password_str = "".join(password[idx] for idx in idx_password)
    print(password_str)
    return password_str

if __name__ == "__main__":
    password_generator()