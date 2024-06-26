'''
Module provides a function that generates a random password

# Gioele Amendola
# 29/04/2024

# Create a function that generates a random password with
# a specified length and desired character types
# (lowercase letters, uppercase letters, numbers, symbols).
# Allow the user to specify the password length and desired character types.
# Generate and return a random password that meets the user's criteria.
'''
# Import of modules
import random
import string


def generate_random_password(length: int = None, desired_char: str | list = None) -> str:
    '''
    Given a length and some desired characters, generatee a random password

    Args:
        length (int, optional): length of password. Defaults to None.
        desired_char (str | list, optional): desired characters. Defaults to None.

    Raises:
        ValueError: if length is not a number greater than 3.

    Returns:
        str: random password generated
    '''

    print("\nGenerating a random password")

    # variable of all characters
    all_characters: str = string.ascii_letters + string.digits + string.punctuation

    # Insert length and desired characters
    # Control for correct inputs
    if length is None:
        while True:
            try:
                length = int(input("Insert length > "))
                if length <= 3:
                    raise ValueError
            except ValueError:
                print("Value Inserted not Valid.")
            else:
                break

    if desired_char is None:
        while True:
            try:
                desired_char = list(
                    input("Insert desired characters (press enter for none) >"))
                if desired_char:
                    if len(desired_char) > length:
                        raise ValueError
            except ValueError:
                print("Value Inserted not Valid.")
            else:
                break
    elif desired_char is str:
        desired_char = list(desired_char)

    # Random password
    # Generate a random length password based on all_characters
    password: str = ''.join(random.choices(all_characters, k=length))
    # Check if desired characters has been inserted
    if desired_char is not None:
        # Creation of a list that has unique random numbers in it for password index
        index_list: list = []
        while len(index_list) < len(desired_char):
            x: int = random.randrange(0, len(password))
            if x not in index_list:
                index_list.append(x)
        # Replace of characters in password string
        for char, i in zip(desired_char, range(len(index_list))):
            password = password[:index_list[i]] + \
                char + password[index_list[i]+1:]

    return password


# Example Test:
pass_length: int = 10
pass_desired_char: str = "p3'!.DD1"

print(generate_random_password(pass_length, pass_desired_char))
print(generate_random_password(), end="\n\n")
