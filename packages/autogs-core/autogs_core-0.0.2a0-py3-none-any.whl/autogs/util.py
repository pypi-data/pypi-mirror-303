import random
import string


def generate_random_string(length: int = 8) -> str:
    """
    Generate a random lowercase string of fixed length.

    Args:
        - length: Length of the string

    Returns:
        - Random lowercase string
    """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))
