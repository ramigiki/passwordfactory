import string
import random


def get_characters(**kwargs):
    """
    Gets the request dict in the params and alter the algorithm

    Returns:
        characters (list): List of all chars enabled in features
    """

    characters = list()
    if kwargs.get("numbers"):
        characters.extend(list(string.digits))
    if kwargs.get("lowercase"):
        characters.extend(list(string.ascii_lowercase))
    if kwargs.get("uppercase"):
        characters.extend(list(string.ascii_uppercase))
    if kwargs.get("symbols"):
        characters.extend(list(string.punctuation))
    return characters


def generate_password(**kwargs):
    """
    Gets the request params and pass it to get_characters()

    Returns:
        password (string): password generated

    """
    length = kwargs.get("length")
    characters = get_characters(**kwargs)
    random.shuffle(characters)
    password = ""
    for i in range(length):
        char = random.choice(characters)
        password = password + char
    return password
